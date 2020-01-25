def solution(s):
    stack_list = []
    for chars in s:
        if len(stack_list) > 0 and stack_list[-1] == chars:
            stack_list.pop()
        else:
            stack_list.append(chars)
    if len(stack_list) == 0:
        return 1
    else:
        return 0
