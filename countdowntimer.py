import time


def countdown_timer(remaining_time):
    for x in range(remaining_time,0,-1):
        secs = x % 60
        minutes = int(x / 60) % 60
        hours = int(x/3600) % 60
    
        print(f"{hours:02}:{minutes:02}:{secs:02}",end="\r")
        time.sleep(1)  
    print("TIME'S UP")
    

def main():
    my_time = int(input("enter the time inseconds"))
    countdown_timer(my_time)
    
    
if __name__ == "__main__":
    main()