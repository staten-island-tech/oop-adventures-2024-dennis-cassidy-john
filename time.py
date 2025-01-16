import time

class Time():
    def __init__(self, time, clock):
        self.time = time
        self.clock = clock
    def __str__(self):
        return self.format_time()

    def format_time(self):
        hours, remainder = divmod(self.time, 3600)
        minutes, seconds = divmod(remainder, 60)
        if self.clock == "HH:MM:SS":
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        elif self.clock == "MM:SS":
            return f"{minutes:02}:{seconds:02}"
        elif self.clock == "SS":
            return f"{self.time} seconds"
        else:
            raise ValueError("Unsupported clock format!")

    def countdown(self):
        while self.time > 0:
            print(self.format_time(), end="\r") 
            time.sleep(1)  
            self.time -= 1  
        print("Time's up!")  

timer = Time(60, "MM:SS")
timer.countdown()