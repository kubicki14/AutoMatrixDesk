import regex as re
import snowboydecoder
import sys
import signal
import subprocess

interrupted = False
fan_status = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def illuminate_columbus():
    print('ACTIVATE MACHINE LEARNING...')
    outlet_state = str(subprocess.check_output(['python', 'tp-link.py', '-t', '192.168.30.212', '-c', 'info']))
    on_off_state = re.search(r'relay_state":(0|1),', outlet_state, re.IGNORECASE).group(1)
    if '1' in on_off_state:
        # This means the switch is on, lets turn it off.
        lightsOff = subprocess.Popen('python tp-link.py -t 192.168.30.212 -c off', shell=True)
    else:
        # This means switch is off (relay_state=0), so turn it on.
        lightsOn = subprocess.Popen('python tp-link.py -t 192.168.30.212 -c on', shell=True)
    return

def led_show():
    # subprocess.run('python app.py', timeout=5)
    try:
        print ('Welcome Lane. Engaging turbines and LED''s...')
        led_output = subprocess.check_output('./everloop_demo', stderr=subprocess.STDOUT, timeout=10)
    except subprocess.TimeoutExpired:
        print('Ending LED show...')
    return

def compass():
    # subprocess.run('python app.py', timeout=5)
    try:
        print ('Transforming LED array (RED=NORTH) -> Compass...')
        led_output = subprocess.check_output('./compass_demo', stderr=subprocess.STDOUT, timeout=10)
    except subprocess.TimeoutExpired:
        print('Ending Compass')
    return

def desk_power():
    print('Turning on/off power to desk/workstation...')
    outlet_state = str(subprocess.check_output(['python', 'tp-link.py', '-t', '192.168.30.146', '-c', 'info']))
    on_off_state = re.search(r'relay_state":(0|1),', outlet_state, re.IGNORECASE).group(1)
    if '1' in on_off_state:
        # This means the switch is on, lets turn it off.
        station_off = subprocess.Popen('python tp-link.py -t 192.168.30.146 -c off', shell=True)
    else:
        # This means switch is off (relay_state=0), so turn it on.
        station_on = subprocess.Popen('python tp-link.py -t 192.168.30.146 -c on', shell=True)
    return

def tequila():
    print('Playing Tequila by The Champs...')
    #play_tequila = subprocess.call(['omxplayer', '-o', 'alsa:chrisspeaker', '--pos', '100', 'tequila.mp3'])
    play_t = subprocess.Popen(['omxplayer', '-o', 'alsa:chrisspeaker', '--pos', '100', 'tequila.mp3'])
    return

def fan_my_fingers():
    print('Toggling fan to keep them fingers from sweating ;)')
    global fan_status
    if not fan_status:
        y = subprocess.call(['sudo', './usb_toggle_power', '-h', '0', '-P', '2', '-p', '1'])
        fan_status = True
    else:
        fan_status = False
        y = subprocess.call(['sudo', './usb_toggle_power', '-h', '0', '-P', '2', '-p', '0'])

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Fan status above set to false, disabling usb ports for fan demo
xRando = subprocess.call(['sudo', './usb_toggle_power', '-h', '0', '-P', '2', '-p', '0'])


# Instantiate the sound models that we will use. Make these on the kitt.ai/snowboy site.
models = ['illuminate.pmdl', 'led_show.pmdl', 'compass.pmdl', 'desk_power.pmdl', 'tequila.pmdl', 'fan_my_fingers.pmdl']
sensitivity = [0.5]*len(models)

detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity, audio_gain=1)
print('Listening... Press Ctrl+C to exit')

# For multiple models add a trigger 'task' to the list
callbacks = [illuminate_columbus, led_show, compass, desk_power, tequila, fan_my_fingers]
# main loop
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
