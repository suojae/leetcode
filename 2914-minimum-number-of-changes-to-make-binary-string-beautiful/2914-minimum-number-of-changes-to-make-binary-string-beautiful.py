class Solution:
    # def minChanges(self, s: str) -> int:
    #    check_count = 0
    #    input_legnth = len(s)
    #    before_char_list = []

    # def evaluate_even(array: List) -> bool:
    #    array_count = len(array)
    #    return array_count % 2 == 0
        

    #    for index in range(0, input_length):
    #        if before_char_list[-1] != s[index]:
    #            if evaluate_even(before_char_list):
    #                before_char_list = []
    #            else: 
    #                check_count+=1
    #                before_char_list.append(1 if s[index] == 0 else 0)
        
        
    #    return check_count

    def minChanges(self, s: str) -> int:
        min_changes_required = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                min_changes_required += 1
        return min_changes_required