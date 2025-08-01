from playsound import playsound 
import threading
import time
import sys

def typing(text,delay=0.05):
    for char in text:
        sys.stdout.write(char) 
        sys.stdout.flush()
        time.sleep(delay)
    print()

threading.Thread(target=playsound,args=(r"C:\Users\mohan\Music\sad-violin-367924.mp3",),daemon=True).start()

lyrics=["i was doing fine without ya ","till i saw your face now i cant erase","bearing into all ths bullshit","is this what you want is this who you are"]
for line in lyrics:
    typing(line,delay=0.06)
    time.sleep(0.1)
