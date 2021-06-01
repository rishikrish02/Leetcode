"""
Reverse the string using python 

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
               
        back  = len(s)-1
        
        for front in range(0,len(s)/2):
            temp = s[front]
            s[front] = s [back]
            s[back] = temp;
            
            back-=1
            
        return s
            

