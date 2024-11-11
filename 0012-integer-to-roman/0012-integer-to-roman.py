class Solution:
    def intToRoman(self, num: int) -> str:
        answer_array = []
        while num > 0:
            if num >= 1000:
                answer_array.append("M")
                num -= 1000
                continue
            if num >= 900:
                answer_array.append("CM")
                num -= 900
                continue
            if num >= 500:
                answer_array.append("D")
                num -= 500
                continue
            if num >= 400:
                answer_array.append("CD")
                num -= 400
                continue
            if num >= 100:
                answer_array.append("C")
                num -= 100
                continue
            if num >= 90:
                answer_array.append("XC")
                num -= 90
                continue
            if num >= 50:
                answer_array.append("L")
                num -= 50
                continue
            if num >= 40:
                answer_array.append("XL")
                num -= 40
                continue
            if num >= 10:
                answer_array.append("X")
                num -= 10
                continue
            if num >= 9:
                answer_array.append("IX")
                num -= 9
                continue
            if num >= 5:
                answer_array.append("V")
                num -= 5
                continue
            if num >= 4:
                answer_array.append("IV")
                num -= 4
                continue
            if num >= 1:
                answer_array.append("I")
                num -= 1
                continue
        return ''.join(answer_array)
