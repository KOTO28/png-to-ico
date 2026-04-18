import os
import sys
from PIL import Image

input_path = "input.png"
output_path = "output.ico"

if not os.path.isfile(input_path):
	print(f"Input file not found: {input_path}", file=sys.stderr)
	sys.exit(1)

img = Image.open(input_path).convert("RGBA")

sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

img.save(output_path, format="ICO", sizes=sizes)
