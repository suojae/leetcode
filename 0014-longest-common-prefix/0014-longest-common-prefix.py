class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            char = strs[0][i]  
            if all(word[i] == char for word in strs):
                answer += char
            else:
                break  

        return answer if answer else ""
