# Intel TBB (Threading Building Blocks)
cc_library(
    name = "onetbb",
    srcs = glob([
        "src/tbb/*.cpp",
        "src/tbbmalloc/*.cpp",
    ], exclude = [
        "src/tbb/main.cpp",
        "src/tbbmalloc/proxy.cpp",
    ]),
    hdrs = glob([
        "include/**/*.h",
    ]),
    includes = [
        "include",
        "src/tbb",
        "src/tbbmalloc",
    ],
    copts = [
        "-Wno-sign-compare",
        "-Wno-unused-parameter",
        "-fPIC",
    ],
    linkopts = ["-lpthread"],
    visibility = ["//visibility:public"],
)