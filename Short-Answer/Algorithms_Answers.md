#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) Linear Time. The `a` variable is Constant Time (O(1)) and the while loop is linear (O(n)). In the **worst case scenario**, it is Linear Time. 


b) O(n^2) because the while loop can run `n` times within the for loop, as the for loop also runs for `n` times. It's an iterative solution.


c) O(n) - Linear time because it's going to _recursively_ call itself for the amount of input of bunnies, until it goes down to zero.

## Exercise II

Start at the halfway point between all the floors of the building.

If the egg breaks, that floor is too high up for the safety of the egg. Set that floor level to the right in the array. 

Assuming the egg broke, go down 1 floor and drop the egg again. If the egg isn't broken when dropped from a certain floor level, place that floor to the left. 

Worst case version of this scenario involves going through halfway of the building, minus the one floor we already tested. 

If the egg does _not_ break, all floors below the current one is considered safe. We then go halfway back up between that range of floors. 

In this solution, I'm using Binary Search - O(log n).