#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

The runtime is O(n) because as the loop checks if "a" is less than n^3, it would
take "n" times to iterate through the entire loop, which is just a linear function
runtime. The runtime will also increase linearly as the input sixe of "n" increases,
since there is a another, successive value in the list.


b) O(n log n)

The runtime is O(n log n) because the outer loop is looping through "n", while
the inner loop is loop through log "n" since the data is split and compared.


c) O(n)

The runtime is O(n) since the function is being recursively called "n" times --
or in this case, "bunnies" time -- and reduces the bunnies by a constant (1) each
time.


## Exercise II

Given the inherent binary nature of the problem (if floor is f or higher, break; 
if floor is f or lower, not break) it makes the most sense to use a binary search
with runtime of O(log n). This makes the problem easier to solve because you are
looking for the phase transition between breaking and not breaking the egg depending
on the current floor. So we are testing if the middle floor breaks the egg when
dropped, if not, we know that we need to move up a level and see if it breaks
at that level; conversely we can also continually halve the bottom (left) and
top (right) floors of the building to find the point at which the egg transitions
from not breaking to breaking, or vice versa.


Pseudocode:

def binary_search_egg(building, floor_f):
    # set bottom_f = 0
    # set top_f = len(building) - 1
    # while the bottom_f <= top_f
        # find the middle_f
        # if the eggs breaks at floor_f
            # check the floors between the bottom_f and the middle_f
        # if the eggs don't break at floor_f
            # check the floors between the middle_f and the top_f

