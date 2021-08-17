import datetime
import time
x = datetime.datetime.now()
y = x.strftime("The time is %I:%M:%S")

while True:
    print(y)
    time.sleep(1)