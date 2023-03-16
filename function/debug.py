import datetime

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

def message(text):
    with open('debug.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{date_time}]: {text}" + "\n")
        print(f"[{date_time}]: {text}")

def save(i):
    with open("setting.txt", "w") as file:
        file.write(str(i + 1))

def getLine():
    with open('setting.txt', 'r') as f:
        data = f.read()
    return data