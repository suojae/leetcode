class Solution:
    def maxScore(self, s: str) -> int:
        # 엣지 케이스: 길이가 1인 경우
        if len(s) <= 1:
            return 0

        # 엣지 케이스: 문자열이 모두 같은 경우
        if s == "0" * len(s) or s == "1" * len(s):
            return len(s) - 1

        max_value = 0
        left_count = 0
        right_count = s.count("1")  # 초기 right_count 설정

        # 슬라이딩 윈도우로 왼쪽/오른쪽 점수 계산
        for i in range(len(s) - 1):  # 마지막 문자 전까지만 반복
            if s[i] == "0":
                left_count += 1  # 왼쪽의 "0" 개수 증가
            elif s[i] == "1":
                right_count -= 1  # 오른쪽의 "1" 개수 감소

            # 현재 점수 계산
            current_score = left_count + right_count
            max_value = max(max_value, current_score)

        return max_value
