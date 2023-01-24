#### approach to count the number of islands using disjoint sets

1) Initialize result (count of islands) as 0 
2) Traverse each index of the 2D matrix. 
3) If the value at that index is 1, check all its 8 neighbours. If a neighbour is also equal to 1, take the union of the index and its neighbour. 
4) Now define an array of size row*column to store frequencies of all sets. 
5) Now traverse the matrix again. 
6) If the value at index is 1, find its set. 
7) If the frequency of the set in the above array is 0, increment the result be 1.
