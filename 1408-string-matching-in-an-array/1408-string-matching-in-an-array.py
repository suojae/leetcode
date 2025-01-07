class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        answer = []

        sorted_words = sorted(words, key=len)
        
        for i in range(len(sorted_words)-1):
            for j in range(i+1, len(sorted_words)):
                if sorted_words[i] in sorted_words[j]:
                    answer.append(sorted_words[i])
                    break
                
        return answer
        