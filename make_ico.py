from PIL import Image

img = Image.open("input.png").convert("RGBA")

sizes = [(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]

img.save("output.ico", format="ICO", sizes=sizes)
