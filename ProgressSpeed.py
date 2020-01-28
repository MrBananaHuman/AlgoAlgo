def solution(progresses, speeds):
    answer = []
    progress = []
    for i in range(0, len(progresses)):
        progress.append(math.ceil((100-progresses[i])/speeds[i]))
    print(progress)
    max_num = progress[0]
    prog_num = 1
    for i in range(1, len(progress)):
        if progress[i] > max_num:
            answer.append(prog_num)
            max_num = progress[i]
            prog_num = 1
            continue
        else:
            prog_num += 1
    answer.append(prog_num)
    return answer

print(solution([93,30,55], [1,30,5]))
