from neurosity import neurosity_sdk
from dotenv import load_dotenv
import os
import sys

load_dotenv()
neurosity = neurosity_sdk({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
})
neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

original_stdout = sys.stdout

def run(et):
    f = open('brainwave/data/' + et + '.log', 'w')

    def callback(data):
        if data != None:
            sys.stdout = f  # Change the standard output to the file we created.
            print(data)
            sys.stdout = original_stdout  # Reset the standard output to its original value
            print(data)

    neurosity.brainwaves_raw(callback)