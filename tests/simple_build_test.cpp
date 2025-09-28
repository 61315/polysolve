#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <polysolve/Types.hpp>
#include <polysolve/Utils.hpp>
#include <Eigen/Dense>
#include <nlohmann/json.hpp>
#include <spdlog/spdlog.h>

TEST_CASE("Bazel build system works", "[bazel]") {
    SECTION("Basic dependencies are available") {
        // Test Eigen
        Eigen::Vector3d v(1, 2, 3);
        REQUIRE(v.norm() > 0);
        
        // Test nlohmann/json
        nlohmann::json j;
        j["test"] = "value";
        REQUIRE(j["test"] == "value");
        
        // Test spdlog
        spdlog::info("Bazel build test successful!");
        
        REQUIRE(true); // If we get here, all dependencies loaded successfully
    }
    
    SECTION("PolySolve utilities are available") {
        // Test that we can access PolySolve types and utilities
        using namespace polysolve;
        
        // This tests that the Types.hpp is accessible
        // Just creating a simple json object to test the types
        nlohmann::json config;
        config["solver"] = "test";
        
        REQUIRE(!config.empty());
    }
}