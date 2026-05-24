class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(int)
        
        for indexs, s in enumerate(strs):
            count = [0] * 26
            
            for indexc, c in enumerate(s):
                count_index = ord(c) - 97
                count[count_index] += 1 

            key = tuple(count)     


            if key not in ans:
                ans[key] = []
            ans[key].append(s)        


        print(list(ans.values()))
        return list(ans.values())


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if not countS[c] == countT.get(c, 0):
                return False

        return True
'''