from  PIL import Image

matrix = Image.open('word_matrix.png')

mask = Image.open('mask.png')

print(matrix.size)
print(mask.size)

mask = mask.resize ((1015,559))
mask.putalpha(150)

matrix.paste(mask,(0,0), mask)

matrix.show()