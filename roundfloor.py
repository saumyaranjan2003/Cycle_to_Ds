#Python has libraries to provide more advanced operations and calculations.
#One of the most common is the math library. math allows you to perform rounding with floor and ceil, 
#provide the value of pi, and numerous other operations. Let's see how to use this library for rounding up or down.
#Rounding numbers enables you to remove the decimal portion of a float. 
#You can choose to always round up to the nearest whole number by using ceil, or down by using floor.

from math import ceil, floor
round_up = ceil(12.5)
print(round_up)
round_down = floor(12.5)
print(round_down)
