# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.10.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.10.1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp"

# Include any dependencies generated for this target.
include CMakeFiles/prime_sieve.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/prime_sieve.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/prime_sieve.dir/flags.make

CMakeFiles/prime_sieve.dir/prime_sieve.cc.o: CMakeFiles/prime_sieve.dir/flags.make
CMakeFiles/prime_sieve.dir/prime_sieve.cc.o: prime_sieve.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/prime_sieve.dir/prime_sieve.cc.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/prime_sieve.dir/prime_sieve.cc.o -c "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/prime_sieve.cc"

CMakeFiles/prime_sieve.dir/prime_sieve.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/prime_sieve.dir/prime_sieve.cc.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/prime_sieve.cc" > CMakeFiles/prime_sieve.dir/prime_sieve.cc.i

CMakeFiles/prime_sieve.dir/prime_sieve.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/prime_sieve.dir/prime_sieve.cc.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/prime_sieve.cc" -o CMakeFiles/prime_sieve.dir/prime_sieve.cc.s

CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.requires:

.PHONY : CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.requires

CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.provides: CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.requires
	$(MAKE) -f CMakeFiles/prime_sieve.dir/build.make CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.provides.build
.PHONY : CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.provides

CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.provides.build: CMakeFiles/prime_sieve.dir/prime_sieve.cc.o


# Object files for target prime_sieve
prime_sieve_OBJECTS = \
"CMakeFiles/prime_sieve.dir/prime_sieve.cc.o"

# External object files for target prime_sieve
prime_sieve_EXTERNAL_OBJECTS =

prime_sieve: CMakeFiles/prime_sieve.dir/prime_sieve.cc.o
prime_sieve: CMakeFiles/prime_sieve.dir/build.make
prime_sieve: CMakeFiles/prime_sieve.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable prime_sieve"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/prime_sieve.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/prime_sieve.dir/build: prime_sieve

.PHONY : CMakeFiles/prime_sieve.dir/build

CMakeFiles/prime_sieve.dir/requires: CMakeFiles/prime_sieve.dir/prime_sieve.cc.o.requires

.PHONY : CMakeFiles/prime_sieve.dir/requires

CMakeFiles/prime_sieve.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/prime_sieve.dir/cmake_clean.cmake
.PHONY : CMakeFiles/prime_sieve.dir/clean

CMakeFiles/prime_sieve.dir/depend:
	cd "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles/prime_sieve.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/prime_sieve.dir/depend
