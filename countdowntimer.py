import time

my_time = int(input("enter the time inseconds"))

for x in range(my_time,0,-1):
    secs = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600) % 60
    
    print(f"{hours:02}:{minutes:02}:{secs:02}",end="\r")
    time.sleep(1)
    
print("TIME'S UP")