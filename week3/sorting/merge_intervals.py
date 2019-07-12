'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return []

        intervals.sort(key=lambda x: x[0])
        res, i = [], 0

        while i < len(intervals) - 1 :
            current_inter = intervals[i]
            next_inter = intervals[i+1]

            if current_inter[-1] < next_inter[0]:
                res.append(current_inter)
            else:
                temp_min = min(min(current_inter), min(next_inter))
                temp_max = max(max(current_inter), max(next_inter))
                next_inter[0] = temp_min
                next_inter[1] = temp_max

            i += 1

        res.append(intervals[-1])
        return res
