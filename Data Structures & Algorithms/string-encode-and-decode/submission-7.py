class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            seperator = str(str(len(word))+"#")
            print(seperator)
            encoded_string += seperator + word
        print(encoded_string)
        return encoded_string
    
    
    def decode(self, s: str) -> List[str]:
        strs = []
        print(s)
        
        i = 0
        sepnum = 0
        while i < len(s):
            if s[i].isnumeric():    
                j = i
                while s[j] != '#':
                    j += 1
                length = int(s[i:j])
                
                strs.append(s[j+1:j+1+length])
                i = j + 1 + length
            else:
                i += 1
        

        return strs