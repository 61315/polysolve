cc_library(
    name = "jse",
    hdrs = glob([
        "include/**/*.hpp",
    ]),
    includes = ["include"],
    deps = [
        "@nlohmann_json//:nlohmann_json",
        "@spdlog//:spdlog",
    ],
    visibility = ["//visibility:public"],
)