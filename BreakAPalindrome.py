##https://leetcode.com/problems/break-a-palindrome/submissions/
"""
check letter one by one from 1 to n/2, if this letter>a, just change it to a and break,
else if this letter ==a, then add this letter to result and keep iterate, if you have reached to the half way,
    1. if it is odd number, you can never change palindrome[n/2] to make it non-panlin, this panlindrom must look like aaaaLetteraaaa,
    under this circumstances, just change last one to "b"

    2. if is even number, then if this letter in the middle is "a", just change the last letter to "b", if it is not "a", then
    just change this letter to "a"
"""

import string
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        re = ""
        n = len(palindrome)
        if n==1:
            return re
        for i in range(int(n/2 + n%2)):
            index = string.ascii_lowercase.index(palindrome[i])
            if i < int(n/2 + n%2 -1):
                if index>0:
                    re += "a"
                    re += palindrome[i+1:]
                    break
                else:
                    re += palindrome[i]

            else:
                if (n%2 == 0 and index ==0) or n%2 ==1:
                    re = palindrome[:-1] + "b"

                elif n%2 == 0 and index >0:
                    re += "a"
                    re += palindrome[i+1:]

        return re

