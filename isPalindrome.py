class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False  # negative numbers can't be palindromes

        else:
            res = [int(x) for x in str(x)]

        left = 0 
        right = len(res) - 1
        while left < right:
            if res[left] != res[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        
