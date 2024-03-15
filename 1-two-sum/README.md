<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?


# Solution
## Intuition
### This approach uses a concept called "complements", where instead of checking every possible pair of numbers in the list, we only need to check for one specific value (the complement) for each number.
## Approach
#### The code is trying to find two numbers in a given list that add up to a target number.
#### It does this by creating a dictionary called "num_indices" which will store the indices of each number as it iterates through the list.
#### For each number in the list, it checks if its complement (the difference between the target and that number) is already in the dictionary.
#### If it is, then we have found our two numbers and their indices are returned.
#### If not, then we add that number and its index to the dictionary so that we can check for its complement later on.
#### This approach uses a concept called "complements", where instead of checking every possible pair of numbers in the list, we only need to check for one specific value (the complement) for each number.
#### This makes the algorithm more efficient as it reduces the time complexity from O(n^2) to O(n).
#### Another important concept used here is dictionaries or hash tables.
#### These data structures allow us to quickly lookup values based on keys, making them useful for storing information like indices in this case.
#### Overall, this solution utilizes concepts such as iteration, conditionals, dictionaries/hashing and time complexity optimization to efficiently solve the problem at hand.
#### The code takes in a list of integers and a target integer, and returns the indices of two numbers in the list that add up to the target, if such a pair exists.
#### If there is no such pair, an empty list is returned.

## Complexity
### Time complexity:
#### O(n)

### Space complexity:
#### O(n)
