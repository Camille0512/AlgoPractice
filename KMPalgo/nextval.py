s = "ababaabab"

def encode_next(input_st):
    '''
    The logic is, two pointers, one is used for progressing, one is used for trace.
    If the progressing pointer equals to the trace pointer, then the both progressing pointer and the trace pointer increase.
    If the progressing pointer does not equals to the trace pointer, then the progressing pointer stays and the trace pointer trace back according to the next array value until they equal to each other.
    :param input_st: the target encoded string
    :return: next value of the encoded string
    '''
    forward = 0
    backward = 1
    next = [0, 0] # The next list position should also be start with 1, therefore add a placeholder at the front
    strlen = len(input_st)
    input_st = " " + input_st # alter the string position, because the calculation should be start with 1

    while backward < strlen:
        if input_st[forward] == input_st[backward] or forward==0:
            forward += 1
            backward += 1
            next.append(forward)
        else:
            forward = next[forward]
    return next[1:] # delete the placeholder before return

res = encode_next(s)
print('next res:', res)

def encode_nexteval(input_str, next):
    '''
    The logic is to use the next to record the place index to be input into the nexteval.
    First we should have the input string and the corresponding next array.
    If the position of the string and the next position of the string equals, then use the next position as the nexteval position and return the corresponding value in the nexteval array to the current nexteval array.
    If the position of the string and the next position of the string differs, the use the next position to return the next vale to the nexteval position.
    :param input_str: the target encoded string
    :param next: the next array correspond to the input string
    :return: the nexteval array
    '''
    next.insert(0, 0)
    nexteval = [0] * len(next)
    input_str = " " + input_str
    for n in range(1, len(next)):
        if input_str[n] == input_str[next[n]]:
            nexteval[n] = nexteval[next[n]]
        else:
            nexteval[n] = next[n]
    return nexteval[1:]

res = encode_nexteval(s, res)
print("nexteval res:", res)