class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fb=-10**9
        sb=-10**9
        fs=0
        ss=0
        for p in prices:
            fb=max(fb,-p)
            fs=max(fs,fb+p)
            sb=max(sb,fs-p)
            ss=max(ss,sb+p)
        return ss