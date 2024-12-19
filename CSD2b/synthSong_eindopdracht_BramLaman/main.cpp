#include <iostream>
#include "audioToFile.h"
#include "customCallback.h"


#define WRITE_TO_FILE

int main() {
    ScopedMessageThreadEnabler scopedMessageThreadEnabler;
    CustomCallback audioSource (44100);
    JUCEModule juceModule (audioSource);
    juceModule.init(1,1);

#if WRITE_TO_FILE
    AudioToFile audioToFile;
    audioToFile.write (audioSource);
#else


    std::cout << "Press q + Enter to quit..." << std::endl;
    bool running = true;
    while (running) {
        switch (std::cin.get()) {
        case 'q':
            running = false;
            break;
        }
    }
#endif
    return 0;
}