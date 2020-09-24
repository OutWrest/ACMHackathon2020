from PIL import Image, ImageDraw
from dots import dotify
from removenums import removenums


# Colden Hall
CH_FL2 = (((58.60*12)/1461) + ((62.01*12)/1527))/2


img = Image.open('CH_3FL.png')
img_dots = dotify(img, CH_FL2, dist=(6*12))
img_dots.save('3Fl_d.png')


img = Image.open('CH3120.jpg')
img = removenums(img)
img = dotify(img, CH_FL2, dist=(3*12))
img.show()
#img.save('CH3120_d.png')





