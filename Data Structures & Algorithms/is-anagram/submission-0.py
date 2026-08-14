class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        # Store the frequency of s character into object 
        count = {}

        for char in s:
                count[char] = count.get(char,0) + 1
        
        # Remove characters according to t
        for char in t:
            if char not in count:
                return False
            
            count[char] = count[char] - 1; 

            if count[char] < 0:
                return False
            
        return True
