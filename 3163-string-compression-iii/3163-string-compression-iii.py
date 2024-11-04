class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        word_count = len(word)
        answer_array = []

        for index in range(1, word_count):
            if word[index - 1] == word[index]:
                if count == 9:
                    answer_array.append(9)
                    answer_array.append(word[index])
                    count = 1
                else:
                    count += 1
            else:
                answer_array.append(count)
                answer_array.append(word[index - 1])
                count = 1

        # 마지막 남은 문자 처리
        answer_array.append(count)
        answer_array.append(word[-1])

        return ''.join(str(item) for item in answer_array)
