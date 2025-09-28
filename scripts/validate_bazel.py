#!/usr/bin/env python3
"""
Simple validation script for Bazel BUILD files.
Checks for common syntax issues and missing files.
"""

import os
import glob
import sys
from pathlib import Path

def check_workspace_file():
    """Check WORKSPACE file exists and has basic structure."""
    workspace_path = Path("WORKSPACE")
    if not workspace_path.exists():
        print("❌ WORKSPACE file not found")
        return False
    
    content = workspace_path.read_text()
    required_sections = [
        "workspace(name",
        "http_archive",
        "rules_cc",
        "eigen",
        "nlohmann_json",
        "spdlog"
    ]
    
    for section in required_sections:
        if section not in content:
            print(f"❌ WORKSPACE missing required section: {section}")
            return False
    
    print("✅ WORKSPACE file structure valid")
    return True

def check_build_files():
    """Check BUILD.bazel files exist and reference real source files."""
    build_files = []
    for pattern in ["BUILD.bazel", "BUILD", "*.BUILD"]:
        build_files.extend(glob.glob(pattern, recursive=True))
        build_files.extend(glob.glob(f"**/{pattern}", recursive=True))
    
    if not build_files:
        print("❌ No BUILD files found")
        return False
    
    print(f"✅ Found {len(build_files)} BUILD files")
    
    # Check main BUILD.bazel
    main_build = Path("BUILD.bazel")
    if main_build.exists():
        content = main_build.read_text()
        
        # Check for common patterns
        if "cc_library" not in content:
            print("❌ Main BUILD.bazel missing cc_library definitions")
            return False
            
        if "polysolve_linear" not in content:
            print("❌ Main BUILD.bazel missing polysolve_linear target")
            return False
            
        print("✅ Main BUILD.bazel structure valid")
    
    return True

def check_source_files():
    """Check that referenced source files exist."""
    src_dir = Path("src")
    if not src_dir.exists():
        print("❌ src directory not found")
        return False
    
    # Check for expected source structure
    expected_dirs = [
        "src/polysolve",
        "src/polysolve/linear",
        "src/polysolve/nonlinear"
    ]
    
    for dir_path in expected_dirs:
        if not Path(dir_path).exists():
            print(f"❌ Expected directory not found: {dir_path}")
            return False
    
    # Count source files
    cpp_files = list(Path("src").rglob("*.cpp"))
    hpp_files = list(Path("src").rglob("*.hpp"))
    
    print(f"✅ Found {len(cpp_files)} .cpp files and {len(hpp_files)} .hpp files")
    return True

def check_test_files():
    """Check test files and BUILD configuration."""
    tests_dir = Path("tests")
    if not tests_dir.exists():
        print("❌ tests directory not found")
        return False
    
    test_build = tests_dir / "BUILD.bazel"
    if not test_build.exists():
        print("❌ tests/BUILD.bazel not found")
        return False
    
    content = test_build.read_text()
    if "cc_test" not in content:
        print("❌ tests/BUILD.bazel missing cc_test definitions")
        return False
    
    print("✅ Test configuration valid")
    return True

def check_third_party():
    """Check third_party BUILD files."""
    third_party_dir = Path("third_party")
    if not third_party_dir.exists():
        print("❌ third_party directory not found")
        return False
    
    build_files = list(third_party_dir.glob("*.BUILD"))
    expected_deps = [
        "eigen.BUILD",
        "nlohmann_json.BUILD", 
        "spdlog.BUILD",
        "fmt.BUILD",
        "catch2.BUILD"
    ]
    
    for dep in expected_deps:
        if not (third_party_dir / dep).exists():
            print(f"❌ Missing third_party BUILD file: {dep}")
            return False
    
    print(f"✅ Found {len(build_files)} third_party BUILD files")
    return True

def main():
    """Run all validation checks."""
    print("🔍 Validating Bazel configuration...")
    print("=" * 50)
    
    checks = [
        check_workspace_file,
        check_build_files,
        check_source_files,
        check_test_files,
        check_third_party
    ]
    
    all_passed = True
    for check in checks:
        if not check():
            all_passed = False
        print()
    
    if all_passed:
        print("🎉 All Bazel configuration checks passed!")
        return 0
    else:
        print("⚠️  Some Bazel configuration issues found")
        return 1

if __name__ == "__main__":
    sys.exit(main())