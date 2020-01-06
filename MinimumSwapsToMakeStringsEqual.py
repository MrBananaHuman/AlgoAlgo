class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_to_y_change_cnt = 0
        y_to_x_change_cnt = 0
        if len(s1) != len(s2):
            return -1
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                x_to_y_change_cnt += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                y_to_x_change_cnt += 1

        if (x_to_y_change_cnt + y_to_x_change_cnt) % 2 != 0:
            return -1
                
        if x_to_y_change_cnt % 2 == 0:
            return int((x_to_y_change_cnt + y_to_x_change_cnt)/2)
        else:
            return int((x_to_y_change_cnt + y_to_x_change_cnt)/2) + 1
                
