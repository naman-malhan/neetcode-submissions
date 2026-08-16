class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in resDict:
                resDict[key] = []
            resDict[key].append(word)
        return list(resDict.values())