class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable_s= {}
        hashtable_t = {}

        for char in s:
            if char in hashtable_s:
                hashtable_s[char] += 1 
            else:
                hashtable_s[char] = 1

        for char in t:
            if char in hashtable_t:
                hashtable_t[char] += 1
            else:
                hashtable_t[char] = 1 

        return hashtable_s == hashtable_t
            

anagram = Solution()
anagram.isAnagram(s="racecar", t="carrace")
            