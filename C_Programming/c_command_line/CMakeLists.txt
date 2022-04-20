cmake_minimum_required(VERSION 3.8)

project(TestCode)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 11)

set(CMAKE_C_FLAGS_RELEASE "-O2 -s -DNDEBUG -Wall -fsanitize=address -fsanitize=leak -fno-omit-frame-pointer")
set(CMAKE_CXX_FLAGS_RELEASE "-O2 -s -DNDEBUG -Wall -fsanitize=address -fsanitize=leak -fno-omit-frame-pointer")
set(CMAKE_C_FLAGS_DEBUG "-O0 -g -Wall")

add_subdirectory(googletest)
include_directories(googlemock/include googletest/include)

enable_testing()

if (EXISTS "Solution/TestCode.c")
    set(TEST_SOURCES testcases.cpp testcases.h Solution/TestCode.c TestCode.h)
else()
    set(TEST_SOURCES testcases.cpp testcases.h TestCode.c TestCode.h)
endif()

set(TEST_SOURCES testcases.cpp testcases.h TestCode.c TestCode.h)

add_executable(TestCode ${TEST_SOURCES})
target_link_libraries(TestCode gtest_main gmock_main)
