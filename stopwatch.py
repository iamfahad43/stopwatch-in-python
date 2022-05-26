import time
import msvcrt
while True:
        user_input = input("Press Enter to start stopwatch and press spacebar to stop the stopwatch")
        start_time=time.time()
        print("Stopwatch has started")
        while True:
            print("Time elapsed:",round(time.time()-start_time,0),'secs',end='\n')
            time.sleep(1)
            if msvcrt.kbhit():
                if ord(msvcrt.getch()) == 32:
                    print("Timer has stopped")
                    end_time=time.time()
                    print("The time elapsed:",round(end_time-start_time,2),'secs')
                    break
       
       