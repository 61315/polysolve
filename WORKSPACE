workspace(name = "polysolve")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

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
    sha256 = "d69f9deb6a75e2580465c6c4c5111b89c4dc2fa94e3a85fcd2ffcd9a143d9273",
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
    sha256 = "5dea48d1fcddc3ec571ce2058e13910a0d4a6bab4cc09a809d8b1dd1c88ae6f2",
    strip_prefix = "fmt-9.1.0",
    urls = [
        "https://github.com/fmtlib/fmt/archive/refs/tags/9.1.0.tar.gz",
    ],
)

# Catch2 testing framework
http_archive(
    name = "catch2",
    build_file = "//:third_party/catch2.BUILD",
    sha256 = "06dbc7620e3b96c2b69d57bf337028bf245a211b3cddb843835bfe258f427a52",
    strip_prefix = "Catch2-2.13.9",
    urls = [
        "https://github.com/catchorg/Catch2/archive/refs/tags/v2.13.9.tar.gz",
    ],
)

# finite-diff library
git_repository(
    name = "finite_diff",
    build_file = "//:third_party/finite_diff.BUILD",
    tag = "v1.0.2",
    remote = "https://github.com/zfergus/finite-diff.git",
)

# LBFGSpp library
git_repository(
    name = "lbfgspp",
    build_file = "//:third_party/lbfgspp.BUILD",
    tag = "v0.4.0",
    remote = "https://github.com/yixuan/LBFGSpp.git",
)

# Spectra eigenvalue library
git_repository(
    name = "spectra",
    build_file = "//:third_party/spectra.BUILD",
    commit = "v1.0.1",
    remote = "https://github.com/yixuan/spectra.git",
)

# PolySolve test data
git_repository(
    name = "polyfem_data",
    remote = "https://github.com/polyfem/polyfem-data",
    commit = "9c1bdd5bd02215e80bc1668547e5dbeb5484a527",
    build_file_content = """
filegroup(
    name = "test_data",
    srcs = glob(["**/*.mat"]),
    visibility = ["//visibility:public"],
)
""",
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
    commit = "11d028ebf54c3665e1a7c25d8ac622a8cb851223",
    remote = "https://github.com/geometryprocessing/json-spec-engine.git",
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