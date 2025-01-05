from typing import List
import string

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # 알파벳 인덱스 매핑
        letters = string.ascii_lowercase  
        alphabet_dict = dict(zip(letters, range(26)))  # {'a': 0, 'b': 1, ..., 'z': 25}

        n = len(s)
        diff = [0] * (n + 1)  # 누적 차이 배열

        # 1. shift 연산 적용 (누적 차이 배열)
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        # 2. 누적합 적용하여 변환
        shift = 0
        result = []
        for i, char in enumerate(s):
            shift += diff[i]  # 현재 위치까지의 누적 이동량 계산
            new_index = (alphabet_dict[char] + shift) % 26  # 알파벳 순환 고려
            result.append(letters[new_index])  # 변환된 문자 추가

        return "".join(result)