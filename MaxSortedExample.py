def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def solution(numbers):
    str_nums = []
    for i in numbers:
        str_nums.append(str(i))
    str_nums = sorted(str_nums, key=cmp_to_key(lambda a, b: -1 if str(b)+str(a) < str(a)+str(b) else 1))
    temp = int(''.join(str_nums))
    return str(temp)
