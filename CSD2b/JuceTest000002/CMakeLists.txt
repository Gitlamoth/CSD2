project(JuceTest002 VERSION 0.0.1)
juce_add_console_app(JuceTest002 PRODUCT_NAME "JuceTest002")
target_sources(JuceTest002 PRIVATE main.cpp)
target_compile_definitions(JuceTest002 PRIVATE JUCE_WEB_BROWSER=0 JUCE_USE_CURL=0)

target_link_libraries(JuceTest002
        PRIVATE
        juce::juce_audio_basics
        juce::juce_audio_devices
        juce::juce_audio_formats
        juce::juce_audio_processors

        PUBLIC
        juce::juce_recommended_config_flags
        juce::juce_recommended_warning_flags
)

target_compile_features(JuceTest002 PRIVATE cxx_std_20)