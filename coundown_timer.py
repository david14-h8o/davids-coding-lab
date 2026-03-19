# countdown_timer.py
import time

def countdown(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} sec")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    secs = int(input("Enter seconds: "))
    countdown(secs)
