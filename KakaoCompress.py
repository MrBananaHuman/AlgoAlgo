def solution(msg):
    dictionary = dict()
    dictionary['A'] = 1
    dictionary['B'] = 2
    dictionary['C'] = 3
    dictionary['D'] = 4
    dictionary['E'] = 5
    dictionary['F'] = 6
    dictionary['G'] = 7
    dictionary['H'] = 8
    dictionary['I'] = 9
    dictionary['J'] = 10
    dictionary['K'] = 11
    dictionary['L'] = 12
    dictionary['M'] = 13
    dictionary['N'] = 14
    dictionary['O'] = 15
    dictionary['P'] = 16
    dictionary['Q'] = 17
    dictionary['R'] = 18
    dictionary['S'] = 19
    dictionary['T'] = 20
    dictionary['U'] = 21
    dictionary['V'] = 22
    dictionary['W'] = 23
    dictionary['X'] = 24
    dictionary['Y'] = 25
    dictionary['Z'] = 26
    
    answer = []

    temp = ''
    last_num = 26
    start = 0
    msg += '*'
    for i, chars in enumerate(msg):
        current_term = msg[start:i+1]
        print(i, current_term)
        if current_term in dictionary:
            temp = current_term
        else:
            answer.append(dictionary[temp])
            last_num += 1
            dictionary[current_term] = last_num
            start = i
            temp = msg[i]
    return answer

solution('KAKAO')
