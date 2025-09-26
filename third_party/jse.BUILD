cc_library(
    name = "jse",
    srcs = [
        "src/jse/jse.cpp",
    ],
    hdrs = glob([
        "src/**/*.h",
        "src/**/*.hpp",
    ]),
    includes = ["src"],
    deps = [
        "@nlohmann_json//:nlohmann_json",
        "@spdlog//:spdlog",
    ],
    visibility = ["//visibility:public"],
)