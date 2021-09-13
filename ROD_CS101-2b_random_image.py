import png
import random
import time


w = 3840
h = 2160
c = 256

pixels = []

start = time.time()

for y in range(h):  # rows
    pixels.append([])    

    for x in range(w):  # cols
        color_red = random.randrange(c)
        color_green = random.randrange(c)
        color_blue = random.randrange(c)

        pixels[y].extend( (color_red,color_green,color_blue) )


with open('/tmp/random-image.png', 'wb') as fp:
    image_writer = png.Writer(w, h, greyscale=False)
    image_writer.write(fp, pixels)

print(f"Finished after {time.time() - start} seconds")
