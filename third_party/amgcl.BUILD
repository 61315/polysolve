# https://github.com/ddemidov/amgcl/blob/93827a00fc926d951c75f08fdb1d491912ff7065/.travis/install_boost.sh#L4

load("@rules_cc//cc:cc_library.bzl", "cc_library")

cc_library(
    name = "amgcl",
    hdrs = glob([
        "amgcl/**/*.hpp",
    ]),
    includes = ["."],
    visibility = ["//visibility:public"],
    deps = [
        # "@boost", # i can't afford the whole boost tarball
        "@boost.property_tree",
    ],
)
