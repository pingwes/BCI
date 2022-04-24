from key import key
from scroll import scroll
import time
import threading

def key_run(epoch_t):
    key.run(epoch_t)

def scroll_run(epoch_t):
    scroll.run(epoch_t)

epoch_time = str(int(time.time()))

t1 = threading.Thread(target=key_run, args=(epoch_time,))
t2 = threading.Thread(target=scroll_run, args=(epoch_time,))

t1.start()
t2.start()
t1.join()
t2.join()

print("Done!")