# Class08B Demos

from PIL import Image
import voronoi_slow as vs

## Steps to produce Voronoi Art

# TODO: 1. load a base image
im = Image.open("parkPhoto.jpg")

# TODO: 2. set a density and choose the centers
density = 0.01 # a density of points, represents how detailed the art is
ctrs = vs.centers(im, density)

# TODO: 3a. prepare the output image
imOut = Image.new('RGB',(im.width,im.height),(255,255,255))

# TODO: 3b. iterate over pixels, setting the color of the output image
pix = imOut.load()
for x in range(imOut.width):
    for y in range(imOut.height):
        pix[x,y] = ctrs.nearest_center_colour((x,y))
        
# TODO: 4. save the output image
imOut.save('outputs/vorPark01.jpg')

# TODO: 5. What does this code do?

for c in ctrs.ctrs:
    x,y = c.pt
    for i in [x-2,x-1,x,x+1,x+2]:
        for j in [y-2,y-1,y,y+1,y+2]:
            if i >= 0 and j >= 0 and i < imOut.width and j < imOut.height:
                pix[i,j] = (255,0,0)

# TODO: 5b. Save the new output image
# imOut.save('outputs/vorPark02.jpg')
