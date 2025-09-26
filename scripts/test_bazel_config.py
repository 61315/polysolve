#!/usr/bin/env python3
"""
Comprehensive test script for Bazel configuration.
Tests build file structure, dependency mapping, and source file coverage.
"""

import os
import re
import sys
import glob
from pathlib import Path

def test_workspace_dependencies():
    """Test WORKSPACE file has all necessary dependencies."""
    print("🔍 Testing WORKSPACE dependencies...")
    
    workspace_path = Path("WORKSPACE")
    if not workspace_path.exists():
        print("❌ WORKSPACE file not found")
        return False
    
    content = workspace_path.read_text()
    
    # Expected dependencies from the CMake build
    required_deps = {
        'eigen': ['Eigen3', 'linear algebra'],
        'nlohmann_json': ['JSON', 'parsing'],
        'spdlog': ['logging', 'fmt'],
        'fmt': ['formatting', 'spdlog dependency'],
        'catch2': ['testing', 'unit tests'],
        'lbfgspp': ['optimization', 'nonlinear'],
        'finite_diff': ['finite differences', 'numerical'],
        'spectra': ['eigenvalue', 'optional'],
        'amgcl': ['multigrid', 'optional'],
        'boost': ['C++ libraries', 'optional'],
        'jse': ['JSON specification', 'validation'],
        'onetbb': ['threading', 'TBB'],
    }
    
    missing_deps = []
    for dep_name, description in required_deps.items():
        if dep_name not in content:
            missing_deps.append(dep_name)
            print(f"❌ Missing dependency: {dep_name} ({', '.join(description)})")
    
    if missing_deps:
        print(f"❌ Found {len(missing_deps)} missing dependencies")
        return False
    
    print(f"✅ All {len(required_deps)} required dependencies found in WORKSPACE")
    return True

def test_main_build_targets():
    """Test main BUILD.bazel has correct library targets."""
    print("\n🔍 Testing main BUILD targets...")
    
    build_path = Path("BUILD.bazel")
    if not build_path.exists():
        print("❌ Main BUILD.bazel not found")
        return False
    
    content = build_path.read_text()
    
    # Expected targets based on CMake structure
    expected_targets = [
        'polysolve_linear',  # Core linear solver library
        'polysolve',         # Full library with nonlinear solvers
        'polysolve_full',    # Combined with optional features
    ]
    
    # Optional feature targets
    optional_targets = [
        'polysolve_linear_with_amgcl',
        'polysolve_linear_with_spectra',
        'polysolve_linear_with_tbb',
    ]
    
    missing_targets = []
    for target in expected_targets:
        if f'name = "{target}"' not in content:
            missing_targets.append(target)
            print(f"❌ Missing target: {target}")
    
    found_optional = 0
    for target in optional_targets:
        if f'name = "{target}"' in content:
            found_optional += 1
    
    if missing_targets:
        print(f"❌ Missing {len(missing_targets)} required targets")
        return False
    
    print(f"✅ All {len(expected_targets)} required targets found")
    print(f"✅ Found {found_optional}/{len(optional_targets)} optional targets")
    return True

def test_source_file_coverage():
    """Test that BUILD files reference existing source files."""
    print("\n🔍 Testing source file coverage...")
    
    # Find all source files
    src_files = {
        'cpp': list(Path('src').rglob('*.cpp')),
        'hpp': list(Path('src').rglob('*.hpp')),
        'h': list(Path('src').rglob('*.h')),
        'tpp': list(Path('src').rglob('*.tpp')),
    }
    
    total_files = sum(len(files) for files in src_files.values())
    print(f"📁 Found {total_files} source files:")
    for ext, files in src_files.items():
        print(f"   - {len(files)} .{ext} files")
    
    # Read main BUILD.bazel
    build_path = Path("BUILD.bazel")
    build_content = build_path.read_text()
    
    # Extract glob patterns
    glob_patterns = re.findall(r'"([^"]*\*[^"]*)"', build_content)
    print(f"📋 Found {len(glob_patterns)} glob patterns in BUILD.bazel")
    
    # Check key directories are covered
    expected_dirs = [
        'src/polysolve',
        'src/polysolve/linear',
        'src/polysolve/nonlinear',
    ]
    
    coverage_good = True
    for dir_path in expected_dirs:
        dir_files = list(Path(dir_path).glob('*.cpp')) + list(Path(dir_path).glob('*.hpp'))
        if dir_files:
            # Check if directory is covered by glob patterns
            covered = any(
                dir_path.replace('src/', '') in pattern or 
                dir_path in pattern or
                '**' in pattern
                for pattern in glob_patterns
            )
            if not covered:
                print(f"❌ Directory {dir_path} may not be covered by BUILD patterns")
                coverage_good = False
            else:
                print(f"✅ Directory {dir_path} appears to be covered")
    
    return coverage_good

def test_dependency_structure():
    """Test that dependencies are correctly structured."""
    print("\n🔍 Testing dependency structure...")
    
    build_path = Path("BUILD.bazel")
    content = build_path.read_text()
    
    # Check for key dependencies mentioned in BUILD file
    key_deps = [
        '@eigen//:eigen',
        '@nlohmann_json//:nlohmann_json', 
        '@spdlog//:spdlog',
        '@jse//:jse',
        '@lbfgspp//:lbfgspp',
        '@finite_diff//:finite_diff',
    ]
    
    found_deps = 0
    for dep in key_deps:
        if dep in content:
            found_deps += 1
            print(f"✅ Found dependency: {dep}")
        else:
            print(f"❌ Missing dependency: {dep}")
    
    if found_deps < len(key_deps):
        print(f"❌ Only found {found_deps}/{len(key_deps)} expected dependencies")
        return False
    
    print(f"✅ All {len(key_deps)} key dependencies found")
    return True

def test_test_configuration():
    """Test test BUILD configuration."""
    print("\n🔍 Testing test configuration...")
    
    test_build_path = Path("tests/BUILD.bazel")
    if not test_build_path.exists():
        print("❌ tests/BUILD.bazel not found")
        return False
    
    content = test_build_path.read_text()
    
    # Check for test files mentioned in CMake
    expected_test_files = [
        'main.cpp',
        'test_linear_solver.cpp',
        'test_nonlinear_solver.cpp',
        'test_json.cpp',
    ]
    
    # Check test sources exist
    tests_dir = Path("tests")
    missing_test_files = []
    for test_file in expected_test_files:
        test_path = tests_dir / test_file
        if not test_path.exists():
            missing_test_files.append(test_file)
            print(f"❌ Missing test file: {test_file}")
        else:
            print(f"✅ Found test file: {test_file}")
    
    # Check if test files are referenced in BUILD
    for test_file in expected_test_files:
        if test_file in content:
            print(f"✅ Test file {test_file} referenced in BUILD")
        else:
            print(f"⚠️  Test file {test_file} not explicitly referenced in BUILD")
    
    # Check for cc_test targets
    test_targets = re.findall(r'cc_test\s*\(\s*name\s*=\s*"([^"]+)"', content)
    print(f"✅ Found {len(test_targets)} test targets: {', '.join(test_targets)}")
    
    return len(missing_test_files) == 0 and len(test_targets) > 0

def test_third_party_builds():
    """Test third_party BUILD files."""
    print("\n🔍 Testing third_party BUILD files...")
    
    third_party_dir = Path("third_party")
    if not third_party_dir.exists():
        print("❌ third_party directory not found")
        return False
    
    build_files = list(third_party_dir.glob("*.BUILD"))
    print(f"📦 Found {len(build_files)} third_party BUILD files")
    
    # Test each BUILD file has correct structure
    valid_builds = 0
    for build_file in build_files:
        content = build_file.read_text()
        if 'cc_library' in content or 'alias' in content:
            print(f"✅ {build_file.name}: Has cc_library or alias")
            valid_builds += 1
        else:
            print(f"❌ {build_file.name}: Missing cc_library or alias")
    
    return valid_builds == len(build_files)

def test_configuration_files():
    """Test configuration files exist and are valid."""
    print("\n🔍 Testing configuration files...")
    
    config_files = [
        ('.bazelrc', 'Bazel configuration'),
        ('linear-solver-spec.json', 'Linear solver specification'),
        ('nonlinear-solver-spec.json', 'Nonlinear solver specification'),
    ]
    
    all_exist = True
    for filename, description in config_files:
        if Path(filename).exists():
            print(f"✅ Found {filename} ({description})")
        else:
            print(f"❌ Missing {filename} ({description})")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests."""
    print("🧪 Testing Bazel Configuration Comprehensively")
    print("=" * 60)
    
    tests = [
        test_workspace_dependencies,
        test_main_build_targets,
        test_source_file_coverage,
        test_dependency_structure,
        test_test_configuration,
        test_third_party_builds,
        test_configuration_files,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test_func.__name__} failed with exception: {e}")
            failed += 1
        print()
    
    print("=" * 60)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All Bazel configuration tests passed!")
        print("✅ The build system appears to be correctly configured.")
        print("📝 Note: Actual build testing requires network access to download dependencies.")
        return 0
    else:
        print("⚠️  Some configuration issues found.")
        print("🔧 Please fix the issues above before using the Bazel build system.")
        return 1

if __name__ == "__main__":
    sys.exit(main())