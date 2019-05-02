from threading import Thread
import time


def delay_exec(func, n):
    wait = n / 1000
    time.sleep(wait)
    return func()

def hello_world(message):
    print(message)


print("Hey")
#delay_exec(hello_world, 3000)
Thread(target=delay_exec, args=(lambda: hello_world("ok"), 3000)).start()
Thread(target=delay_exec, args=(lambda: hello_world("you"), 2000)).start()
Thread(target=delay_exec, args=(lambda: hello_world("Are"), 1000)).start()
print("This should be printed before every messages above")
