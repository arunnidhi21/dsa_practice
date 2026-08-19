"""
LeetCode 26: Remove Duplicates from Sorted Array
Given a sorted array, remove duplicates in-place so each element
appears only once, and return the new length.

Approach: same insert_pos pattern as Move Zeroes. Walk through the
array starting from index 1, comparing each element to the previous
one. Only copy it forward if it's different from its predecessor
(since the array is sorted, duplicates are always adjacent).

Time: O(n)   Space: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        insert_pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos
