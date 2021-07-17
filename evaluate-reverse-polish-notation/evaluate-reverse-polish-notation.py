import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val=[]
        for t in tokens:
            if t.isdigit() or len(t)>1:
                val.append(int(t))
            elif t=='+':
                val.append(val.pop()+val.pop())
            elif t=='-':
                a=val.pop()
                b=val.pop()
                val.append(b-a)
            elif t=='*':
                val.append(val.pop()*val.pop())
            elif t=='/':
                a=val.pop()
                b=val.pop()
                if b//a<0:
                    val.append(math.ceil(b/a))
                else:
                    val.append(b//a)
        return val[-1]