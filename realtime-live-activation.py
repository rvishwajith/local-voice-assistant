from RealtimeSTT import AudioToTextRecorder
import numpy as np

def process_text(text):
    print(text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(realtime_model_type="large.en")

    while True:
        recorder.text(process_text)