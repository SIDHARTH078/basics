import time
def typing_animation(text,delay=0.1):
    for char in text:
        print(char,end="",flush=True)
        time.sleep(delay)
    print()

lyrics=["i was doing fine without ya ","till i saw your face now i cant erase","bearing into all ths bullshit","is this what you want is this who you are"]

def show_lyrics(lines):
    for line in lines:
        typing_animation(line)
        time.sleep(1.5)
if __name__=="__main__":
    show_lyrics(lyrics)