class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        aux=[]
        for c in s:
            if c.isalnum():
                aux.append(c)
        return aux==aux[::-1]
                