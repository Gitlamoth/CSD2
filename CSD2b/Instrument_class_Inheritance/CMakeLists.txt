cmake_minimum_required(VERSION 3.20)
project(InstrumentClass LANGUAGES CXX)

add_executable(instrumentclassexample main.cpp instrument.cpp instrument.h)
target_compile_features(instrumentclassexample PRIVATE cxx_std_20)