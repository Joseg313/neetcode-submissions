class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for string in strs:
            key = [0] *26

            for letter in string:
                key_index = ord(letter) - 97
                key[key_index] += 1
            
            answer[tuple(key)].append(string)
        
        

        return list(answer.values())