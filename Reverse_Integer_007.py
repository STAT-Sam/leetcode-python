'''
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_int = int(str(abs(x))[::-1])
        if reversed_int >= 2 ** 31 - 1 or x == 0:
            return 0

        return reversed_int * -1 if x < 0 else reversed_int