# Mario_mine
Find the max area through DFS Algorithm

## Description
When Mario mines, he can move up, down, left, or right, but he cannot move diagonally. 
Also, Mario can only mine one type of ore at a time. 

For example, in the given mine map of size 4 x 5, where 0 represents gold ore and 1 represents iron ore, if Mario starts mining from [1,1], he can move up, down, left, or right to mine { [1,0], [1,1], [0,1], [0,2], [1,2] }, which forms an area of 5 units of gold ore. 
If he starts from [0,4], he can only mine { [0,4], [1,4] }, forming an area of 2 units of gold ore, as he cannot move diagonally to [2,3]. 
If Mario starts from [2,0], he can mine { [2,0], [2,1], [2,2], [3,1] }, forming an area of 4 units of iron ore, as he cannot move diagonally to [1,3].

Using the given map as an example, Mario can mine the most gold ore, with an area of 5 units of gold ore. Please help Mario mine the maximum amount of gold or iron ore (find the largest area).

| |0|1|2|3|4|
|-|-|-|-|-|-|
|0|1|0|0|1|0|
|1|0|0|0|1|0|
|2|1|1|1|0|1|
|3|0|1|0|0|1|

## Input
- The input consists of two lines.
- The first line contains the dimensions of the mine map, N and M, separated by a space. The values of N and M satisfy the conditions 1 ≤ N ≤ 1000 and 1 ≤ M ≤ 1000.
- The second line to the (N+1)-th line contains the values of each row of the mine map. Each row contains M boolean values separated by spaces. Here, 1 represents iron ore, and 0 represents gold ore.

## Output
The output is a positive integer K, where K >= 1, representing the area of the largest ore deposit (in terms of grid units).
