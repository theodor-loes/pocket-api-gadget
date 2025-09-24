from pimoroni import RGBLED
import network
import time

def connect_wifi(ssid, password):
    led = RGBLED(6, 7, 8)
    led.set_rgb(2, 2, 2)
    wlan = network.WLAN(network.STA_IF)  # Create a station interface
    wlan.active(True)                    # Activate the interface
    wlan.connect(ssid, password)         # Connect to the specified SSID

    # Wait for connection
    max_wait = 10
    for _ in range(max_wait, 0, -1):
        led.set_rgb(0, 0, 2)
        if wlan.isconnected():
            print('Connected to', ssid)
            print('IP address:', wlan.ifconfig()[0])
            led.set_rgb(0, 2, 0)
            time.sleep(0.5)
            led.set_rgb(0, 0, 0)
            return wlan
        print('Waiting for connection...')
        led.set_rgb(0, 0, 0)
        time.sleep(1)
        
    led.set_rgb(2, 0, 0)
    raise RuntimeError('Failed to connect to Wi-Fi')
