cc_library(
    name = "finite_diff",
    srcs = [
        "src/finitediff.cpp",
    ],
    hdrs = glob([
        "src/*.hpp",
    ]),
    includes = ["src"],
    deps = [
        "@eigen//:eigen",
        "@spdlog//:spdlog",
    ],
    visibility = ["//visibility:public"],
)