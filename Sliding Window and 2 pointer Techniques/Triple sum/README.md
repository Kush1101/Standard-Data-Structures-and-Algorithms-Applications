# Triplet sum
Given an array, find a triplet in the array, such that its sum is equal to a given number.<br>
We look at a naive implementation and an optimized solution using two pointer technique and hashing.<br>
A simple variation to this problem is to find a triplet such that the sum of two is equal to the third.<br>
Here we will use the same technique by first sorting the array and starting from the last element, <br>
we will search for a pair whose sum is equal to that element.<br>
This is an **O(n<sup>2</sup>)** solution.
