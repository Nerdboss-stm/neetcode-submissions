class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for s in tokens:
            if s not in ops:
                stack.append(int(s))
            else:
                tmp1 = stack.pop()  
                tmp2 = stack.pop() 
                if s == '+':
                    stack.append(tmp1+tmp2)
                elif s == '-':
                    stack.append(tmp2-tmp1)
                elif s == '*':
                    stack.append(tmp2*tmp1)
                elif s == '/':
                    stack.append(int(tmp2/tmp1))

        return stack[-1]
                
        
        