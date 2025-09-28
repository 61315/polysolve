cc_library(
    name = "spdlog",
    hdrs = glob([
        "include/**/*.h",
    ]),
    includes = ["include"],
    deps = ["@fmt//:fmt"],
    defines = [
        "SPDLOG_FMT_EXTERNAL",
    ],
    visibility = ["//visibility:public"],
)