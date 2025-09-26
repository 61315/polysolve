cc_library(
    name = "eigen",
    hdrs = glob([
        "Eigen/**",
        "eigen3/**",
        "unsupported/**",
    ], allow_empty = True),
    defines = [
        "EIGEN_MPL2_ONLY",
    ],
    includes = ["."],
    visibility = ["//visibility:public"],
)

# Alias for compatibility
alias(
    name = "Eigen3",
    actual = ":eigen",
    visibility = ["//visibility:public"],
)