# Test functionality of Snowboy API /w python wrapper on raspberry pi /w matrix creator 8 microphone array - Lane Kubicki
import snowboydecoder

def detected_callback():
    print('Lights HAVE BEEN DETECTED. ACTIVATE MACHINE LEARNING')

detector = snowboydecoder.HotwordDetector("lights.pmdl", sensitivity=0.5, audio_gain=1)

detector.start(detected_callback)
