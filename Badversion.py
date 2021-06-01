"""
Find the bad version out of list of
multiple version Implementing in python
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start = 0
        end = n
        mid = 0
        while start <= end:
            mid = (start + end)/2           
            if(isBadVersion(mid)):
                end = mid-1
            else:
                start = mid+1
        return mid
        