def solution(answers):
    answer = []
    one_num = 0
    two_num = 0
    three_num = 0
    one_pattern = [1, 2, 3, 4, 5]
    two_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    three_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, an in enumerate(answers):
        if one_pattern[i % len(one_pattern)] == an:
            one_num += 1
        if two_pattern[i % len(two_pattern)] == an:
            two_num += 1
        if three_pattern[i % len(three_pattern)] == an:
            three_num += 1
    max_num = max(one_num, two_num, three_num)
    if one_num == max_num:
        answer.append(1)
    if two_num == max_num:
        answer.append(2)
    if three_num == max_num:
        answer.append(3)
    
    return answer


answers = [1,3,2,4,2]

print(solution(answers))
