# Contains Nearby Almost Duplicate

Given an integer array `nums` and two integers `k` and `t`, return `True` if there are two distinct indices `i` and `j` in the array such that `abs(nums[i] - nums[j]) <= t` and `abs(i - j) <= k`.

*Example 1:*

    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true

*Example 2:*

    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true

*Example 3:*

    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false

*Constraints:*

    0 <= nums.length <= 2 * 104
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 104
    0 <= t <= 2^31 - 1

