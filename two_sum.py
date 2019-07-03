# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:20:40 2019

@author: shawn

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


"""
Brute force option 1
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = []
        
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in r:
                return [i,nums.index(temp)]
            
            r.append(nums[i])
            

"""
Brute force option 2
"""

class Solution:

    def twoSum(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: List[int]

        """

        for i in nums:

            j = target - i

            tmp_nums_start_index = nums.index(i) + 1

            tmp_nums = nums[tmp_nums_start_index:]

            if j in tmp_nums:

                return [nums.index(i), tmp_nums_start_index + tmp_nums.index(j)]
            
           
        
