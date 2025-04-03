import os
import sys
import subprocess
import json
import gzip
import time
import random
import concurrent.futures
import ssl

# Function to install required modules
def install_dependencies():
    required_modules = ['websocket-client', 'requests']
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"{module} not found, installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# Install dependencies before running the main logic
install_dependencies()

# Import modules after ensuring they are installed
import websocket
import requests

# Initialize counters
created = 0
failed = 0

# Colors for console output
L = '\033[1;33m'  # Yellow
C = "\033[1;97m"  # White
B = '\033[2;36m'  # Cyan
Y = '\033[1;34m'  # Light Blue
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red

# Telegram bot token and chat ID
token = f'7926439558:AAEcaIMxU6aXK8G1qhFJjWVDnL6NVjCKQvE'
id = '6036913753'

# Clear console and display welcome message
os.system('clear')
print(Y + '𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗖𝗮𝘀𝗶𝗻𝗼 𝗦𝗮𝗳𝘂𝗺 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗖𝗿𝗲𝗮𝘁𝗶𝗼𝗻ـ ')
print(C + "∞" * 60)
print("Welcome to the application account creation tool 𝗦𝗮𝗳𝗲𝘂𝗺")
print("𝗧𝗵𝗲 𝗧𝗼𝗼𝗹 𝗪𝗶𝗹𝗹 𝗦𝘁𝗮𝗿𝘁 𝗖𝗿𝗲𝗮𝘁𝗶𝗻𝗴 𝗔𝗰𝗰𝗼𝘂𝗻𝘁𝘀 𝗔𝗳𝘁𝗲𝗿 5 𝗦𝗲𝗰𝗼𝗻𝗱𝘀 ")
time.sleep(5)

# Function to create accounts
def create():
    global created, failed
    ch = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    user = str(random.choice('qwertyuioplkjhgfdsazxcvbnm')[0]) + str(''.join(random.choice(ch) for i in range(7)))

    tlg = f'''  𝗡𝗲𝘄 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗖𝗿𝗲𝗮𝘁𝗲𝗱
⋘─────━━─────⋙
˛ 𝗨𝘀𝗲𝗿  : {user}
˛ 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 : hhhh
⋘─────━━─────⋙
𝗯𝘆 : 𝗚𝗮𝗻𝘀𝘁𝗲𝗿 𝗖𝗮𝘀𝗶𝗻𝗼💀
   '''

    headers = {
        "app": "com.safeum.android",
        "host": None,
        "remoteIp": "134.209.93.148",
        "remotePort": str(8080),
        "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
        "time": "2023-04-30 12:13:32",
        "url": "wss://51.79.208.190/Auth"
    }

    data0 = {
        "action": "Register",
        "subaction": "Desktop",
        "locale": "en_GB",
        "gmt": "+02",
        "password": {
            "m1x": "503c73d12b354f86ff9706b2114704380876f59f1444133e62ca27b5ee8127cc",
            "m1y": "6387ae32b7087257452ae27fc8a925ddd6ba31d955639838249c02b3de175dfc",
            "m2": "219d1d9b049550f26a6c7b7914a44da1b5c931eff8692dbfe3127eeb1a922fcf",
            "iv": "e38cb9e83aef6ceb60a7a71493317903",
            "message": "0d99759f972c527722a18a74b3e0b3c6060fe1be3ad53581a7692ff67b7bb651a18cde40552972d6d0b1482e119abde6203f5ab4985940da19bb998bb73f523806ed67cc6c9dbd310fd59fedee420f32"
        },
        "magicword": {
            "m1x": "04eb364e4ef79f31f3e95df2a956e9c72ddc7b8ed4bf965f4cea42739dbe8a4a",
            "m1y": "ef1608faa151cb7989b0ba7f57b39822d7b282511a77c4d7a33afe8165bdc1ab",
            "m2": "4b4d1468bfaf01a82c574ea71c44052d3ecb7c2866a2ced102d0a1a55901c94b",
            "iv": "b31d0165dde6b3d204263d6ea4b96789",
            "message": "8c6ec7ce0b9108d882bb076be6e49fe2"
        },
        "magicwordhint": "0000",
        "login": str(user),
        "devicename": "Xiaomi Redmi Note 8 Pro",
        "softwareversion": "1.1.0.1380",
        "nickname": "hvtctchnjvfxfx",
        "os": "AND",
        "deviceuid": "c72d110c1ae40d50",
        "devicepushuid": "*dxT6B6Solm0:APA91bHqL8wxzlyKHckKxMDz66HmUqmxCPAVKBDrs8KcxCAjwdpxIPTCfRmeEw8Jks_q13vOSFsOVjCVhb-CkkKmTUsaiS7YOYHQS_pbH1g6P4N-jlnRzySQwGvqMP1gxRVksHiOXKKP",
        "osversion": "and_11.0.0",
        "id": "1734805704"
    }

    try:
        ws = websocket.create_connection("wss://51.79.208.190/Auth", header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})
        ws.send(json.dumps(data0))
        result = ws.recv()
        decoded_data = gzip.decompress(result)

        if '"comment":"Exists"' in str(decoded_data):
            failed += 1
        elif '"status":"Success"' in str(decoded_data):
            created += 1
            requests.post(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text={tlg}")
        elif '"comment":"Retry"' in str(decoded_data):
            failed += 1
        else:
            print(decoded_data)
    except Exception as e:
        print(f"Error: {e}")

# Main loop
executor = concurrent.futures.ThreadPoolExecutor(max_workers=500)

while True:
    executor.submit(create)
    os.system('clear')
    print(C + "Make free account for safeUm app ")
    print(L + "∞" * 60)
    print(G + 'Created : ' + str(created))
    print(R + 'Failed : ' + str(failed))
    print(L + "∞" * 60)
    print(C + "𝗚𝗮𝗻𝗴𝘀𝘁𝗲𝗿 𝗖𝗮𝘀𝗶𝗻𝗼")
