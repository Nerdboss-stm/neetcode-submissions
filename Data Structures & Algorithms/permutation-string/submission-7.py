class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # Fill counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts:
            return True
            
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add the new character entering the window
            s2_counts[ord(s2[i]) - ord('a')] += 1
            # Remove the old character leaving the window
            s2_counts[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_counts == s2_counts:
                return True
                
        return False