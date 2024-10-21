from collections import Counter

class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def DFS(curr_string, answer_dictionary):

            if len(curr_string) == 0:
                return len(answer_dictionary)

            max_count = 0

            for i in range(1, len(curr_string) + 1):
                substring = curr_string[:i]

                if substring not in answer_dictionary:
                    answer_dictionary[substring] = True
                    max_count = max(max_count, DFS(curr_string[i:], answer_dictionary))
                    
                    del answer_dictionary[substring]

            return max_count

        return DFS(s, {})
