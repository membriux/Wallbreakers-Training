'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            flag = False
            indx = nums2.index(num)
            for j in range(indx,len(nums2)):
                if num < nums2[j]:
                    result.append(nums2[j])
                    flag = True
                    break
            if flag == False:
                result.append(-1)
        return result
