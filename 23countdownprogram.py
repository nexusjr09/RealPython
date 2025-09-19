#countdown processs
import time
time1 = int(input("Enter the time : "))
for x in reversed(range(0,time1)):
    seconds = x % 60 
    minutes = int(x % 60) % 60 #x / 60 converts total seconds into total minutes.
    #% 60 gives the minutes part after removing hours.
    #Example: 3750 seconds → 3750/60 = 62 minutes → 62 % 60 = 2 minutes.
    hours = hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's Up ")