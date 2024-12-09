# Install script for directory: C:/Users/braml/Documents/CSD2/JUCE

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/CSD")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/braml/Documents/CSD2/build/JUCE/tools/modules/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/braml/Documents/CSD2/build/JUCE/tools/extras/Build/cmake_install.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/JUCE-8.0.4" TYPE FILE FILES
    "C:/Users/braml/Documents/CSD2/build/JUCE/tools/JUCEConfigVersion.cmake"
    "C:/Users/braml/Documents/CSD2/build/JUCE/tools/JUCEConfig.cmake"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/JUCECheckAtomic.cmake"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/JUCEHelperTargets.cmake"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/JUCEModuleSupport.cmake"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/JUCEUtils.cmake"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/JuceLV2Defines.h.in"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/LaunchScreen.storyboard"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/PIPAudioProcessor.cpp.in"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/PIPAudioProcessorWithARA.cpp.in"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/PIPComponent.cpp.in"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/PIPConsole.cpp.in"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/RecentFilesMenuTemplate.nib"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/UnityPluginGUIScript.cs.in"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/checkBundleSigning.cmake"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/copyDir.cmake"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/juce_runtime_arch_detection.cpp"
    "C:/Users/braml/Documents/CSD2/JUCE/extras/Build/CMake/juce_LinuxSubprocessHelper.cpp"
    )
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/Users/braml/Documents/CSD2/build/JUCE/tools/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/Users/braml/Documents/CSD2/build/JUCE/tools/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()