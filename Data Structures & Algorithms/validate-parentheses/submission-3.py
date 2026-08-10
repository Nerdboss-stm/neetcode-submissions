class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {"(","{","["}
        closes = {")","}","]"}
        for bracket in s:
            if bracket in opens :
                stack.append(bracket)
            if bracket in closes :
                if len(stack) == 0:
                    return False
                if bracket == ")" and stack[-1] != "(":
                    return False
                if bracket == "}" and stack[-1] != "{":
                    return False
                if bracket == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        if len(stack) == 0 :
            return True
        else :
            return False

        