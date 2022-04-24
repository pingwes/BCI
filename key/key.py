import pynput
from pynput.keyboard import Key, Listener
import time
charCount = 0
keys = []
import csv
import sys

epoch_time = str(int(time.time()))

original_stdout = sys.stdout # Save a reference to the original standard output

def run(et):
    print("key running")
    with open('key/data/' + epoch_time + '.log', 'w') as f:

        def onKeyPress(key):
            sys.stdout = f  # Change the standard output to the file we created.

            try:
                current_time = str(time.time())

                sys.stdout = f  # Change the standard output to the file we created.
                print('{ "input": "key_pressed", "key: "' + str(key) + ', "time": ' + current_time + '}')
                sys.stdout = original_stdout
                print('{ "input": "key_pressed", "key: "' + str(key) + ', "time": ' + current_time + '}')

            except Exception as ex:
                print('There was an error : ',ex)

        def onKeyRelease(key):
            current_time = str(int(time.time()))

            sys.stdout = f  # Change the standard output to the file we created.
            print('{ "input": "key_released", "key: "' + str(key) + ', "time": ' + current_time + '}')
            sys.stdout = original_stdout
            print('{ "input": "key_released", "key: "' + str(key) + ', "time": ' + current_time + '}')

        with Listener(on_press=onKeyPress,\
            on_release=onKeyRelease) as listener:
            listener.join()
