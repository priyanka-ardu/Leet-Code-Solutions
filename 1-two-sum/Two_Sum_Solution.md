#Intuition
###This approach uses a concept called "complements", where instead of checking every possible pair of numbers in the list, we only need to check for one specific value (the complement) for each number.
#Approach
###The code is trying to find two numbers in a given list that add up to a target number.
###It does this by creating a dictionary called "num_indices" which will store the indices of each number as it iterates through the list.
###For each number in the list, it checks if its complement (the difference between the target and that number) is already in the dictionary.
###If it is, then we have found our two numbers and their indices are returned.
###If not, then we add that number and its index to the dictionary so that we can check for its complement later on.
###This approach uses a concept called "complements", where instead of checking every possible pair of numbers in the list, we only need to check for one specific value (the complement) for each number.
###This makes the algorithm more efficient as it reduces the time complexity from O(n^2) to O(n).
###Another important concept used here is dictionaries or hash tables.
###These data structures allow us to quickly lookup values based on keys, making them useful for storing information like indices in this case.
###Overall, this solution utilizes concepts such as iteration, conditionals, dictionaries/hashing and time complexity optimization to efficiently solve the problem at hand.
###The code takes in a list of integers and a target integer, and returns the indices of two numbers in the list that add up to the target, if such a pair exists.
###If there is no such pair, an empty list is returned.

#Complexity
##Time complexity:
###O(n)

##Space complexity:
###O(n)
