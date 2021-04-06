class Solution: ##https://leetcode.com/problems/valid-palindrome-ii/submissions/
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        a = 0
        b = n-1

        while a < b and s[a] == s[b]:
            a += 1
            b -= 1
        if a >= b:
            return True

        c = a + 1
        d = b
        while c < d and s[c] == s[d]:
            c += 1
            d -= 1
        if c >= d:
            return True

        e = a
        f = b - 1
        while e < f and s[e] == s[f]:
            e += 1
            f -= 1
        if e >= f:
            return True

        return False

a ="rdsiqgkvzkmhcmrfyizpqfaiwhkaznlhtlvlsjowubyujhwaehssheawhjuybuwojslvlthlnzakhwiaqpziyfrmchmkzvkgqisdr"
