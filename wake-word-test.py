from RealtimeSTT import AudioToTextRecorder

if __name__ == '__main__':
    recorder = AudioToTextRecorder(wake_words="computer", wakeword_backend="pvporcupine")
    print("\n\n\nWait for the model to say speak now.\n")
    print('Say a wake word, then speak.\n\nWake words:')