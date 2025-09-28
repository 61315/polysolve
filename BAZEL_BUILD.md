# Building PolySolve with Bazel

This document describes how to build and test PolySolve using Bazel.

## Prerequisites

1. **Bazel**: Install Bazel or Bazelisk (recommended)
   ```bash
   # Using Bazelisk (automatically manages Bazel versions)
   npm install -g @bazel/bazelisk
   # or
   go install github.com/bazelbuild/bazelisk@latest
   
   # Or install Bazel directly
   # See: https://bazel.build/install
   ```

2. **System Dependencies** (for optional features):
   ```bash
   # Ubuntu/Debian
   sudo apt install libblas-dev liblapack-dev libsuitesparse-dev

   # macOS
   brew install openblas lapack suite-sparse
   ```

## Building

### Basic Build Commands

```bash
# Build the linear solver library
bazel build //:polysolve_linear

# Build the full nonlinear solver library
bazel build //:polysolve

# Build with all optional dependencies
bazel build //:polysolve_full
```

### Build Configurations

```bash
# Optimized release build
bazel build --config=opt //:polysolve

# Debug build
bazel build --config=dbg //:polysolve

# Development build (debug + keep going on errors)
bazel build --config=dev //:polysolve
```

### Platform-Specific Builds

```bash
# Linux
bazel build --config=linux //:polysolve

# macOS
bazel build --config=macos //:polysolve
```

## Testing

### Run All Tests

```bash
# Run all unit tests
bazel test //tests:unit_tests

# Run with specific configuration
bazel test --config=opt //tests:unit_tests
```

### Run Individual Test Suites

```bash
# Linear solver tests only
bazel test //tests:linear_solver_test

# Nonlinear solver tests only
bazel test //tests:nonlinear_solver_test

# JSON configuration tests
bazel test //tests:json_test
```

### Testing with Sanitizers

```bash
# Address Sanitizer
bazel test --config=asan //tests:unit_tests

# Thread Sanitizer
bazel test --config=tsan //tests:unit_tests

# Undefined Behavior Sanitizer
bazel test --config=ubsan //tests:unit_tests
```

## Code Coverage

```bash
# Generate coverage report
bazel coverage --config=dbg //tests:unit_tests

# Coverage report will be available at:
# bazel-out/_coverage/_coverage_report.dat
```

## Library Variants

### Core Libraries

- `//:polysolve_linear` - Linear solver library (core)
- `//:polysolve` - Full library including nonlinear solvers

### Optional Feature Libraries

- `//:polysolve_linear_with_amgcl` - With AMGCL support
- `//:polysolve_linear_with_spectra` - With Spectra eigenvalue solver
- `//:polysolve_linear_with_tbb` - With Intel TBB threading
- `//:polysolve_full` - All optional features combined

## Configuration

### Bazel Configuration (.bazelrc)

The build behavior can be customized through `.bazelrc` and `.bazelrc.local`:

```bash
# Copy the sample configuration
cp .bazelrc .bazelrc.local

# Edit local configuration
vim .bazelrc.local
```

### Build Options

Common build flags can be set in `.bazelrc.local`:

```bash
# Enable specific features
build --define=with_mkl=true
build --define=with_cholmod=true

# Custom optimization
build --copt=-march=native
build --copt=-O3
```

## Dependencies

The Bazel build automatically manages the following dependencies:

- **Eigen3** - Linear algebra library
- **nlohmann/json** - JSON parsing and generation
- **spdlog** - Fast logging library
- **fmt** - Formatting library (spdlog dependency)
- **Catch2** - Testing framework
- **LBFGSpp** - L-BFGS optimization
- **finite-diff** - Finite difference computations
- **Spectra** - Eigenvalue computations (optional)
- **AMGCL** - Algebraic multigrid (optional)
- **Intel TBB** - Threading support (optional)
- **JSE** - JSON Specification Engine

## Troubleshooting

### Common Issues

1. **Network Issues**: If external dependencies fail to download:
   ```bash
   bazel clean --expunge
   bazel build --verbose_failures //:polysolve
   ```

2. **Cache Issues**: Clear Bazel cache:
   ```bash
   bazel clean --expunge
   ```

3. **Compiler Issues**: Check compiler compatibility:
   ```bash
   bazel build --verbose_failures --sandbox_debug //:polysolve
   ```

### Debugging Build Issues

```bash
# Verbose build output
bazel build --verbose_failures //:polysolve

# Show all build commands
bazel build --subcommands //:polysolve

# Debug sandbox issues
bazel build --sandbox_debug //:polysolve
```

## Integration with IDE

### VS Code

1. Install the Bazel extension
2. Use `bazel run @hedron_compile_commands//:refresh_all` to generate compile_commands.json

### CLion

CLion has native Bazel support. Open the project directory and select "Bazel" as the build system.

## Continuous Integration

The project includes GitHub Actions workflows for Bazel builds:

- `.github/workflows/bazel.yml` - Main Bazel CI workflow
- Builds on Ubuntu and macOS
- Tests with different configurations (opt, dbg)
- Runs sanitizer tests
- Generates code coverage reports

## Migration from CMake

Both CMake and Bazel builds are supported. Key differences:

| Feature | CMake | Bazel |
|---------|-------|-------|
| Build command | `cmake --build build` | `bazel build //:polysolve` |
| Test command | `ctest` | `bazel test //tests:unit_tests` |
| Configuration | CMakeCache.txt | `.bazelrc` |
| Dependencies | cmake/recipes/ | WORKSPACE + third_party/ |

The Bazel build provides:
- Faster incremental builds
- Better dependency management
- Hermetic builds
- Cross-platform consistency
- Built-in test runner
- Integrated code coverage