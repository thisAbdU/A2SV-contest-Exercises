class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0 for i in range(len(s) + 1)]
        for shift_indx in range(len(shifts)):
            if shifts[shift_indx][2] == 0:
                shift[shifts[shift_indx][0]] -= 1
                shift[(shifts[shift_indx][1]) + 1] += 1
            else:
                shift[shifts[shift_indx][0]] += 1
                shift[(shifts[shift_indx][1]) + 1] -= 1
        for i in range(1, len(shift)):
            shift[i] = shift[i - 1] + shift[i]
        return ''.join(
            chr(ord('a') + (ord(s[i]) - ord('a') + shift[i] + 26) % 26) for i in range(len(s))
        )

