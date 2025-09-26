#include <iostream>
#include <filesystem>
#include <polysolve/Utils.hpp>
#include <unsupported/Eigen/SparseExtra>

int main() {
    const std::string path = POLYFEM_DATA_DIR;
    std::cout << "POLYFEM_DATA_DIR: " << path << std::endl;
    
    // Check if directory exists
    if (std::filesystem::exists(path)) {
        std::cout << "Directory exists!" << std::endl;
        for (const auto& entry : std::filesystem::directory_iterator(path)) {
            std::cout << "  " << entry.path().filename() << std::endl;
        }
    } else {
        std::cout << "Directory does not exist!" << std::endl;
        
        // Try to find it in current directory and subdirectories
        std::cout << "Looking for .mat files in current directory:" << std::endl;
        for (const auto& entry : std::filesystem::recursive_directory_iterator(".")) {
            if (entry.path().extension() == ".mat") {
                std::cout << "  Found: " << entry.path() << std::endl;
            }
        }
        
        // Check for common Bazel runfiles locations
        std::vector<std::string> test_paths = {
            "external/polyfem_data",
            "../polyfem_data", 
            "polyfem_data",
            "./polyfem_data",
            "runfiles/_main/external/polyfem_data",
            "tests.runfiles/_main/external/polyfem_data"
        };
        
        for (const auto& test_path : test_paths) {
            if (std::filesystem::exists(test_path)) {
                std::cout << "Found data at: " << test_path << std::endl;
                if (std::filesystem::exists(test_path + "/A_2.mat")) {
                    std::cout << "  A_2.mat exists at: " << test_path + "/A_2.mat" << std::endl;
                    
                    // Test loadMarket with this path
                    Eigen::SparseMatrix<double> A;
                    const bool ok = Eigen::loadMarket(A, test_path + "/A_2.mat");
                    std::cout << "  loadMarket result: " << (ok ? "SUCCESS" : "FAILED") << std::endl;
                    if (ok) {
                        std::cout << "  Matrix size: " << A.rows() << "x" << A.cols() << std::endl;
                        break;
                    }
                }
            }
        }
    }
    
    return 0;
}