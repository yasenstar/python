from rembg import remove
from PIL import Image

input_path = r"D:\GitHub\python\image\removebg\plane.png"
output_path = r"D:\GitHub\python\image\removebg\plane_nobg.png"

inp = Image.open(input_path)
outp = remove(inp)

outp.save(output_path)