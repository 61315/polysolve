cc_library(
    name = "fmt",
    srcs = glob([
        "src/format.cc",
        "src/os.cc",
    ]),
    hdrs = glob([
        "include/**/*.h",
    ]),
    includes = ["include"],
    defines = ["FMT_SHARED"],
    visibility = ["//visibility:public"],
)