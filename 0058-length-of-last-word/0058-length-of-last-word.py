class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []
        
        for index in range(len(s) - 1, -1, -1):
            if not stack and s[index] == " ":
                continue
            if stack and s[index] == " ":
                return len(stack) 
            stack.append(s[index])

        return len(stack) 
