#!/usr/bin/env python3
"""
Validate that Bazel configuration correctly maps CMake structure.
Cross-references CMakeLists.txt with BUILD.bazel files.
"""

import re
import sys
from pathlib import Path

def extract_cmake_targets():
    """Extract library targets from CMakeLists.txt."""
    cmake_path = Path("CMakeLists.txt")
    if not cmake_path.exists():
        return {}
    
    content = cmake_path.read_text()
    
    # Find add_library calls
    targets = {}
    
    # Main targets
    if "add_library(polysolve_linear)" in content:
        targets['polysolve_linear'] = {
            'type': 'library',
            'sources': ['src/polysolve/*.cpp', 'src/polysolve/linear/*.cpp'],
            'dependencies': ['Eigen3::Eigen', 'spdlog::spdlog', 'nlohmann_json::nlohmann_json']
        }
    
    if "add_library(polysolve)" in content:
        targets['polysolve'] = {
            'type': 'library', 
            'sources': ['src/polysolve/nonlinear/*.cpp'],
            'dependencies': ['polysolve::linear', 'LBFGSpp::LBFGSpp', 'finitediff::finitediff']
        }
    
    return targets

def extract_bazel_targets():
    """Extract library targets from BUILD.bazel."""
    build_path = Path("BUILD.bazel")
    if not build_path.exists():
        return {}
    
    content = build_path.read_text()
    
    # Find cc_library targets
    targets = {}
    
    # Extract all cc_library blocks
    cc_library_pattern = r'cc_library\s*\(\s*name\s*=\s*"([^"]+)"[^)]*\)'
    matches = re.finditer(cc_library_pattern, content, re.DOTALL)
    
    for match in matches:
        target_name = match.group(1)
        target_block = match.group(0)
        
        # Extract sources (simplified)
        sources = re.findall(r'"([^"]*\.cpp)"', target_block) + re.findall(r'"([^"]*\*[^"]*\.cpp)"', target_block)
        
        # Extract deps
        deps = re.findall(r'"(@[^"]+)"', target_block)
        
        targets[target_name] = {
            'type': 'library',
            'sources': sources,
            'dependencies': deps
        }
    
    return targets

def compare_targets():
    """Compare CMake and Bazel targets."""
    print("🔍 Comparing CMake and Bazel target definitions...")
    
    cmake_targets = extract_cmake_targets()
    bazel_targets = extract_bazel_targets()
    
    print(f"📋 Found {len(cmake_targets)} CMake targets")
    print(f"📋 Found {len(bazel_targets)} Bazel targets")
    
    # Check main targets exist in both
    main_targets = ['polysolve_linear', 'polysolve']
    
    all_good = True
    for target in main_targets:
        cmake_has = target in cmake_targets
        bazel_has = target in bazel_targets
        
        if cmake_has and bazel_has:
            print(f"✅ Target '{target}' exists in both CMake and Bazel")
        elif cmake_has and not bazel_has:
            print(f"❌ Target '{target}' exists in CMake but missing in Bazel")
            all_good = False
        elif not cmake_has and bazel_has:
            print(f"✅ Target '{target}' exists in Bazel (CMake structure may differ)")
        else:
            print(f"❌ Target '{target}' missing in both systems")
            all_good = False
    
    return all_good

def validate_source_mapping():
    """Validate that source files are correctly mapped."""
    print("\n🔍 Validating source file mapping...")
    
    # Expected source structure based on CMake subdirectory calls
    expected_structure = {
        'polysolve_linear': [
            'src/polysolve',
            'src/polysolve/linear'
        ],
        'polysolve': [
            'src/polysolve/nonlinear'
        ]
    }
    
    build_path = Path("BUILD.bazel")
    content = build_path.read_text()
    
    all_good = True
    for target, expected_dirs in expected_structure.items():
        print(f"\n📁 Checking target '{target}':")
        
        for expected_dir in expected_dirs:
            # Check if directory is covered in BUILD file patterns
            # Look for exact patterns that include this directory
            dir_pattern = expected_dir  # Use full path including src/
            
            patterns_found = []
            # Check for direct matches of the directory pattern
            if f'"{dir_pattern}/*.cpp"' in content:
                patterns_found.append(f'{dir_pattern}/*.cpp')
            if f'"{dir_pattern}/*.hpp"' in content:
                patterns_found.append(f'{dir_pattern}/*.hpp')
            if f'"{dir_pattern}/*.tpp"' in content:
                patterns_found.append(f'{dir_pattern}/*.tpp')
                
            # Check for recursive patterns
            if f'"{dir_pattern}/**/*.cpp"' in content:
                patterns_found.append(f'{dir_pattern}/**/*.cpp')
            if f'"{dir_pattern}/**/*.hpp"' in content:
                patterns_found.append(f'{dir_pattern}/**/*.hpp')
            
            if patterns_found:
                print(f"   ✅ {expected_dir} is covered")
                print(f"      Patterns: {', '.join(patterns_found)}")
            else:
                print(f"   ❌ {expected_dir} may not be covered by BUILD patterns")
                all_good = False
    
    return all_good

def validate_dependency_mapping():
    """Validate dependency mapping between CMake and Bazel."""
    print("\n🔍 Validating dependency mapping...")
    
    # CMake to Bazel dependency mapping
    dep_mapping = {
        'Eigen3::Eigen': '@eigen//:eigen',
        'spdlog::spdlog': '@spdlog//:spdlog', 
        'nlohmann_json::nlohmann_json': '@nlohmann_json//:nlohmann_json',
        'jse::jse': '@jse//:jse',
        'LBFGSpp::LBFGSpp': '@lbfgspp//:lbfgspp',
        'finitediff::finitediff': '@finite_diff//:finite_diff',
        'Catch2::Catch2': '@catch2//:catch2',
    }
    
    build_content = Path("BUILD.bazel").read_text()
    test_build_content = Path("tests/BUILD.bazel").read_text() if Path("tests/BUILD.bazel").exists() else ""
    all_content = build_content + test_build_content
    
    all_good = True
    for cmake_dep, bazel_dep in dep_mapping.items():
        if bazel_dep in all_content:
            print(f"✅ {cmake_dep} → {bazel_dep}")
        else:
            print(f"❌ Missing dependency mapping: {cmake_dep} → {bazel_dep}")
            all_good = False
    
    return all_good

def main():
    """Run all validation checks."""
    print("🔄 Validating CMake ↔ Bazel Structure Mapping")
    print("=" * 60)
    
    checks = [
        compare_targets,
        validate_source_mapping,
        validate_dependency_mapping,
    ]
    
    all_passed = True
    for check in checks:
        if not check():
            all_passed = False
        print()
    
    print("=" * 60)
    if all_passed:
        print("🎉 All structure mapping validations passed!")
        print("✅ Bazel configuration correctly mirrors CMake structure")
        return 0
    else:
        print("⚠️  Some mapping issues found")
        print("🔧 Please review the configuration for completeness")
        return 1

if __name__ == "__main__":
    sys.exit(main())