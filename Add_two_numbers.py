"""
leetcode problem Two sum
implemented using Hashmap */
"

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sum = 0
        output = []
        d = {}
        
        for i in range(0,len(nums)):
            sum = target - nums[i]
            
            if sum in d.keys():
                output.append(d[sum])
                output.append(i)
            else:
                d[nums[i]] = i 
                
        return output
            




