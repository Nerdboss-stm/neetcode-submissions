class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = "".join(sorted(s1))
        print(s)
        li = []
        n = len(s)
        print(n)
        for l in range(0, len(s2)-n+1):
            li.append(s2[l:l+n])
        print(list)
        ordered_string = ["".join(sorted(word)) for word in li]
        print(ordered_string)
        if s in ordered_string:
            return True
        else:
            return False