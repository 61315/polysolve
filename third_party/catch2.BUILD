cc_library(
    name = "catch2",
    hdrs = glob([
        "single_include/**/*.hpp",
    ]),
    includes = ["single_include"],
    visibility = ["//visibility:public"],
)

# Separate library for the main function
cc_library(
    name = "catch2_main",
    hdrs = glob([
        "single_include/**/*.hpp",
    ]),
    includes = ["single_include"],
    defines = ["CATCH_CONFIG_MAIN"],
    visibility = ["//visibility:public"],
)