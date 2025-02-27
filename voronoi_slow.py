
from PIL import Image
from dataclasses import dataclass, field
import random

@dataclass
class center:
    #TODO: add the fields needed to describe a center
    pass

@dataclass
class centers:

    ctrs: list[center] = field(default_factory=list)

    def __init__(self, img: Image, density: float):
        #when an object of type centers is declared, what should it look like? 
        # populate the list of centers using the given image
        
        pix = img.load()
        self.ctrs = []
        
        #TODO: calculate the number of centres
        num_ctrs = 0
        
        #TODO: find and append all the centres into a list
        pass

    def distance(self, p1: tuple[int,int], p2: tuple[int,int]) -> int:
        # TODO: calculate the squared euclidean distance given two points
        pass
        

    def nearest_center_colour(self, pt: tuple[int,int]) -> tuple[int,int,int]:
        # given a point, returns the colour of the closest center from the list
        
        best_center = self.ctrs[0]
        
        #TODO: Iterate through all centres and determine the closest centre, return that colour
        pass




