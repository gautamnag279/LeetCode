class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not(strs):
            return ""
        pref = ""
        for i in zip(*strs):
            if len(set(i)) != 1:
                return pref
            pref += i[0]
            
        return pref
        
