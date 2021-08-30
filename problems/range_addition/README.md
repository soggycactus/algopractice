# Range Addition

You are given an `m x n` matrix `M` initialized with all `0's` and an array of operations `ops`, where `ops[i]` = [a<sub>i</sub>, b<sub>i</sub>] means `M[x][y]` should be incremented by one for all 0 <= x < a<sub>i</sub> and 0 <= y < b<sub>i</sub>.

Count and return the number of maximum integers in the matrix after performing all the operations.

*Example 1:*

![Example 1](examples/example1.jpg)

    Input: m = 3, n = 3, ops = [[2,2],[3,3]]
    Output: 4
    Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

*Example 2:*

    Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
    Output: 4

*Example 3:*

    Input: m = 3, n = 3, ops = []
    Output: 9

*Constraints:*

- 1 <= m, n <= 4 * 10<sup>4</sup>
- 1 <= ops.length <= 10<sup>4</sup>
- ops[i].length == 2
- 1 <= a<sub>i</sub> <= m
- 1 <= b<sub>i</sub> <= n

