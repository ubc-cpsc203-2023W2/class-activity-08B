
from PIL import Image
from typing import List, Tuple
from dataclasses import dataclass, field
import random



@dataclass
class center:
    # what data characterizes a center?
    
    # TODONE: add the fields needed to describe a center
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
        
        #TODONE: calculate the number of centres
        num_ctrs = int(img.width * density * img.height)
        
        #TODONE: find and append all the centres into a list
        for c in range(num_ctrs):
            x = random.randint(0, img.width - 1)
            y = random.randint(0, img.height - 1)
            self.ctrs.append(center((x, y), pix[x, y]))


    def distance(self, p1: Tuple[int,int], p2: Tuple[int,int])-> int:
        # TODONE: calculate the squared euclidean distance given two points

        return ((p1[0]-p2[0])**2) + ((p1[1] - p2[1])**2)

    def nearest_center_colour(self, pt: Tuple[int, int]) -> Tuple[int, int, int]:
        # given a point, returns the color of the closest center from the list
        # pattern computation -- linear search for something in a list
        best_center = self.ctrs[0]
        
        #TODONE: Iterate through all centres and determine the closest centre, return that colour
        for c in self.ctrs:
            # if distance from pt to c.pt is better then replace best_center w c
            if self.distance(pt, c.pt) < self.distance(pt, best_center.pt):
                best_center = c
        return best_center.colour