project(AoC)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_CXX_STANDARD 14)

# Set the minimum version of CMake that can be used
# To find the cmake version run
# $ cmake --version
cmake_minimum_required(VERSION 3.5)

# Add an executable with the above sources
add_executable(part1 src/part1.cpp src/funciones.cpp)
add_executable(test src/test.cpp src/funciones.cpp)

if (EXISTS src/part2.cpp)
add_executable(part2 src/part2.cpp src/funciones.cpp)
target_include_directories(part2
    PRIVATE 
        ${PROJECT_SOURCE_DIR}/include
)
endif()

# Set the directories that should be included in the build command for this target
# when running g++ these will be included as -I/directory/path/
target_include_directories(part1
    PRIVATE 
        ${PROJECT_SOURCE_DIR}/include
)
target_include_directories(test
    PRIVATE 
        ${PROJECT_SOURCE_DIR}/include
)
