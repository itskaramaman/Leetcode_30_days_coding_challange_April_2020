# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

# Solution


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        counts = {0: -1}
        count = 0
        for i in range(len(nums)):
            count = count+1 if nums[i] == 1 else count-1
            if count in counts.keys():
                max_len = max(max_len, i-counts[count])
            else:
                counts[count] = i
        return max_len
