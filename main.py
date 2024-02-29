
from PIL import Image, ImageDraw
from typing import List, Tuple
from dataclasses import dataclass, field
import random



@dataclass
class center:
    # what data characterizes a center?
    pt: Tuple[int, int]
    colour: Tuple[int, int, int]

@dataclass
class centers:

    ctrs: List[center] = field(default_factory=list)

    def __init__(self, img: Image, density: float):
        #when an object of type centers is declared, what should it look
        #like? populate the list of centers using the given image
        pix = img.load()
        self.ctrs = []
        num_ctrs = int(img.width * density * img.height)
        for c in range(num_ctrs):
            x = random.randint(0, img.width - 1)
            y = random.randint(0, img.height - 1)
            self.ctrs.append(center((x, y), pix[x, y]))


    def distance(self, p1: Tuple[int,int], p2: Tuple[int,int])-> int:   # what's a good name?
        return ((p1[0]-p2[0])*(p1[0]-p2[0])) + ((p1[1] - p2[1]) * (p1[1] - p2[1]))

    def nearest_center_colour(self, pt: Tuple[int, int]) -> Tuple[int, int, int]:
        # given a point, returns the color of the closest center from the list
        # pattern computation -- linear search for something in a list
        best_center = self.ctrs[0]
        for c in self.ctrs:
            # if distance from pt to c.pt is better then replace best_center w c
            if self.distance(pt, c.pt) < self.distance(pt, best_center.pt):
                best_center = c
        return best_center.colour




# 1. load a base image
im = Image.open("parkPhoto.jpg")
# 2. choose the centers
ctrs = centers(im, 0.001)  # second param is a density of points
# 3a. prepare the output image
imOut = Image.new('RGB', (im.width, im.height), (255, 255, 255))
# 3b. iterate over pixels, setting the color of the output image
pix = imOut.load()
for x in range(imOut.width):
    for y in range(imOut.height):
        pix[x, y] = ctrs.nearest_center_colour((x, y))


# what does this code do?
# for c in ctrs.ctrs:
#     x,y = c.pt
#     for i in [x-2,x-1,x,x+1,x+2]:
#         for j in [y-2,y-1,y,y+1,y+2]:
#             if i >= 0 and j >= 0 and i < imOut.width and j < imOut.height:
#                 pix[i,j] = (255,0,0)

# 4. save the output image
imOut.save('vorPark02.jpg')
