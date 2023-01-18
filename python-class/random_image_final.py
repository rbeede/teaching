import os
import time
import sys

from PIL import Image



if(len(sys.argv) != 4):
     sys.exit(f"Usage: {sys.argv[0]} width height filename")

w = int(sys.argv[1])
h = int(sys.argv[2])
filename = sys.argv[3]

pixels = []

start = time.time()

pixels = os.urandom(w * h * 3)

print(f"Generated {len(pixels)} random bytes in {time.time() - start} seconds")

random_image = Image.frombytes('RGB', (w, h), pixels)

random_image.save(filename)

print(f"Finished after {time.time() - start} seconds")
