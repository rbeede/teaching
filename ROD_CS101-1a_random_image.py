import png
import secrets
import time


w = 3840
h = 2160
c = 256

pixels = []

start = time.time()

for y in range(h):  # rows
    pixels.append([])    

    for x in range(w):  # cols
        color_red = secrets.randbelow(c)
        color_green = secrets.randbelow(c)
        color_blue = secrets.randbelow(c)

        pixels[y].extend( (color_red,color_green,color_blue) )


with open('/tmp/random-image.png', 'wb') as fp:
    image_writer = png.Writer(w, h, greyscale=False)
    image_writer.write(fp, pixels)

print(f"Finished after {time.time() - start} seconds")
