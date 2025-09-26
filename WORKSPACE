workspace(name = "polysolve")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

# Rules for C++ compilation
http_archive(
    name = "rules_cc",
    sha256 = "2037875b9a4456dce4a79d112a8ae885bbc4aad968e6587dca6e64f3a0900cdf",
    strip_prefix = "rules_cc-0.0.9",
    urls = ["https://github.com/bazelbuild/rules_cc/releases/download/0.0.9/rules_cc-0.0.9.tar.gz"],
)

# Eigen linear algebra library
http_archive(
    name = "eigen",
    build_file = "//:third_party/eigen.BUILD",
    sha256 = "b4c198460eba6f28d34894e3a5710998818515104d6e74e5cc331ce31e46e626",
    strip_prefix = "eigen-3.4.0",
    urls = [
        "https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.bz2",
    ],
)

# nlohmann/json library
http_archive(
    name = "nlohmann_json",
    build_file = "//:third_party/nlohmann_json.BUILD",
    sha256 = "b94997df68856753b72f0d7a3703b7d484d4745c567f3584ef97c96c25a5798e",
    strip_prefix = "json-3.11.2",
    urls = [
        "https://github.com/nlohmann/json/archive/refs/tags/v3.11.2.tar.gz",
    ],
)

# spdlog logging library
http_archive(
    name = "spdlog",
    build_file = "//:third_party/spdlog.BUILD",
    sha256 = "ca5cae8d6cac15dae0ec63b21d6ad3530070650f68076f3a4a862ca293a858bb",
    strip_prefix = "spdlog-1.11.0",
    urls = [
        "https://github.com/gabime/spdlog/archive/refs/tags/v1.11.0.tar.gz",
    ],
)

# fmt library (dependency of spdlog)
http_archive(
    name = "fmt",
    build_file = "//:third_party/fmt.BUILD",
    sha256 = "78b8c0a72b1c35e4443a7e308df52498252d1cefc2b08c9a97bc9ee6cfe61f8b",
    strip_prefix = "fmt-9.1.0",
    urls = [
        "https://github.com/fmtlib/fmt/archive/refs/tags/9.1.0.tar.gz",
    ],
)

# Catch2 testing framework
http_archive(
    name = "catch2",
    build_file = "//:third_party/catch2.BUILD",
    sha256 = "4e8db9bead3cd3c29b4d8dd5ded18a2c13a6d3d50b2374146a5c8b4e2bdc51c7",
    strip_prefix = "Catch2-2.13.9",
    urls = [
        "https://github.com/catchorg/Catch2/archive/refs/tags/v2.13.9.tar.gz",
    ],
)

# finite-diff library
git_repository(
    name = "finite_diff",
    build_file = "//:third_party/finite_diff.BUILD",
    commit = "v1.0.2",
    remote = "https://github.com/zfergus/finite-diff.git",
)

# LBFGSpp library
git_repository(
    name = "lbfgspp",
    build_file = "//:third_party/lbfgspp.BUILD",
    commit = "v0.2.0",
    remote = "https://github.com/yixuan/LBFGSpp.git",
)

# Spectra eigenvalue library
git_repository(
    name = "spectra",
    build_file = "//:third_party/spectra.BUILD",
    commit = "v1.0.1",
    remote = "https://github.com/yixuan/spectra.git",
)

# AMGCL library
git_repository(
    name = "amgcl",
    build_file = "//:third_party/amgcl.BUILD",
    commit = "1.4.3",
    remote = "https://github.com/ddemidov/amgcl.git",
)

# Boost libraries (minimal set for the project)
http_archive(
    name = "boost",
    build_file = "//:third_party/boost.BUILD",
    sha256 = "6478edfe2f3305127cffe8caf73ea0176c53769f4bf1585be237eb30798c3b8e",
    strip_prefix = "boost_1_83_0",
    urls = [
        "https://archives.boost.io/release/1.83.0/source/boost_1_83_0.tar.bz2",
    ],
)

# JSON Specification Engine library
git_repository(
    name = "jse",
    build_file = "//:third_party/jse.BUILD",
    commit = "main",  # Update to specific tag when available
    remote = "https://github.com/polyfem/json-spec-engine.git",
)

# Intel TBB (Threading Building Blocks)
http_archive(
    name = "onetbb",
    build_file = "//:third_party/onetbb.BUILD",
    sha256 = "e5b57537c741400cf6134b428fc1689a649d7d38d9bb9c1b6d64f092ea28178a",
    strip_prefix = "oneTBB-2021.9.0",
    urls = [
        "https://github.com/oneapi-src/oneTBB/archive/refs/tags/v2021.9.0.tar.gz",
    ],
)