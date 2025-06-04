# Rohith Vishwajith
# 
# test.py
# Tests of realtime STT using manual activation. Should transcribe all recorded speech
# into text upon clicking enter or stopping speaking depending on the example.
# 
# To run:
# Make sure ffmpeg is installed before running, or else it will not work and won't give
# you an error message (on macOS)
#
# source .venv/bin/activate
# python3 test.py
# 
# Make sure the following are installed in the environment:
# ffmpeg
# realtime-stt (pip3 install RealtimeSTT)
# openwakeword (pip)
# pywizlight (pip)

from RealtimeSTT import AudioToTextRecorder

def process_text(text):
    print(text)

if __name__ == '__main__':
    recorder = AudioToTextRecorder()
    print("Created realtime STT recorder.")

    def standalone_test():
        print("\n\n\nRunning standalone test.")
        recorder.start()
        input("Press Enter to stop recording...")
        recorder.stop()
        print("Stopped recording.\nTranscription: ", recorder.text())
    
    def automatic_recording():
        print("\n\n\nRunning automatic detection. Speak to start transcribing.")
        print("\nTranscribed text:")
        with AudioToTextRecorder() as recorder:
            print(recorder.text())

    # standalone_test()
    automatic_recording()