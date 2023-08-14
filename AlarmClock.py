import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            frequency = 2500  # Set frequency (Hz)
            duration = 2000  # Set duration (ms)
            winsound.Beep(frequency, duration)
            break
        time.sleep(1)  # Check the time every 1 second

if __name__ == "__main__":
    print("Welcome to the Alarm Clock!")
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")

    try:
        time.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS format.")
