# Flatten Nested List

Given a deeply-nested array of integers `nums`, return the flattened array of nums. Assume the list can be potentially infinitely nested.

Example 1:

    Input: nums = [1, 2, [1, 2]]
    Output: [1, 2, 1, 2]

Example 2:

    Input: nums = [1, 2, 3, [1, 2, 3, [1, [[[3, 4, [5]]]]]]]
    Output: [1, 2, 3, 1, 2, 3, 1, 3, 4, 5]

Example 3:

    Input: [1, 1, 1, 1, 1]
    Output: [1, 1, 1, 1, 1]

Example 4:

    Input: []
    Output: []

Example 5:

    Input: nums = [[[[4, 5, [6, 7, [[[8, 9]]]]]]]]
    Output: [4, 5, 6, 7, 8, 9]