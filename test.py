# from pathlib import Path
# current_dir = Path.cwd()

# file:Path = ''
# # Find all files in current directory that end with ".png"
# png_files = list(current_dir.glob('*.png'))

# # Print the names of the files found
# print(current_dir, type(current_dir))
# for file in png_files:
#     print(file.name)

# file = str(current_dir/file.name)
# print(file)
# print()
# from PIL import Image
# import pytesseract

# img = Image.open(file)
# text = pytesseract.image_to_string(img)
# # Print the extracted text
# print(text)




from PIL import Image
from pytesseract import *

class Test:
    def __init__(self, path:str):
        test_img_path = path
        test_img = Image.open(test_img_path)
        img_txt = image_to_string(test_img, lang='eng+kor', config='--psm 1 -c preserve_interword_spaces=1')

        with open('test_sample(2).txt', 'w', encoding='utf-8-sig') as tx:
            tx.write(img_txt)


if __name__ == "__main__":
    test = Test(path="captured_image.png")