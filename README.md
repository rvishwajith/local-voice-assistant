# A fully-local, open-source voice assistant.
A local voice assistant I'm working on using whisper / whisper-live and realtime-stt for realtime speech transcription, local LLM interfacing via Haystack, and realtime-tts for spoken responses. Some test files with speech transcription and wake work detection using openwakeword are available. Ensure all of the prerequisite libraries are installed.

Once speech recognition is more accurate, feed the transcribed voice input into a local LLM (probably Qwen 1.5B for lower-end / non-cuda devices) and provide a list of compatible devices and commands.

## Dependencies
Make sure the following are installed in your python environment:
ffmpeg
realtime-stt (pip3 install RealtimeSTT)
openwakeword (pip3 install OpenWakeWord)
pywizlight (pip3 install pywizlight)

## Performance

Every part of this will probably run much better on:
- Best: A CUDA device with a dedicated GPU and at least 4GB VRAM (preferably 8+)
- Good: An ARM device with at least 12GB shared RAM.
- Ok: A device with a dedicated AMD GPU will be slower regardless of GPU power, because CUDA is not supported.
- Bad: A non-ARM CPU-only device / a device with integrated graphics.

## How it works

Have the LLM handle listing functions and paramaters, i.e.:
1. Human: [says something with openwakeword keyword]
2. RealtimeSTT: Converted text: "[keyword, ex. computer], turn on the lights"
3. Main loop: Provide text to LLM:
   command = "turn on the lights"
   lightIDs = [wiz_1, wiz_shelf_lamp, wiz_desk_lamp, fridge_light]
   turn_on_light(lightID)
   set_light_brightness(lightID, brightness)
   set_light_color(lightID, #HEXCOL)
5. LLM prompt: Provide previous data from main loop.
   Given these devices and functions, list the functions that need to be executed following the provided format. Provide a 1-2 sentence summary of what the actions do in the format, "Okay, I'll do [X]".
6. Execute the functions listed by the LLM using some arbitrary API mapped from the list and whatever given devices are being operated on:
   Ex. Philips WIZ API
   For fully local control, map to Home Assistant functions.
7.  Use realtime TTS to say the summary provided by LLM.
