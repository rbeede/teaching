import os
import time

from PIL import Image

w = 3840
h = 2160
c = 256

pixels = []

start = time.time()

pixels = os.urandom(w * h * 3)

print(f"Generated random in {time.time() - start} seconds")

random_image = Image.frombytes('RGB', (w, h), pixels)

random_image.save('/tmp/random-image.png')

print(f"Finished after {time.time() - start} seconds")
