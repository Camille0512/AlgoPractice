s = "we will we will r u"

def count_str_frequency(input_str):
    res_dict = {}
    for i in input_str:
        res_dict[i] = res_dict.get(i) + 1 if res_dict.get(i) else 1
    return res_dict

res = count_str_frequency(s)
print('res:', res)
print("vals res:", sorted(set(res.values()), reverse=True))

def restructure_dict_val(input_dict):
    dict_sorted_val = sorted(set(input_dict.values()), reverse=True) # To sort the dictionary value in an descending way.
    new_dict = {}
    for i in dict_sorted_val:
        tmp = [j for j in input_dict if input_dict[j]==i]
        new_dict[i] = tmp
    return new_dict

new_res = restructure_dict_val(res)
print("new dict res:", new_res)
# new_res[3] = ["testing"]
# print("Testing:", new_res)
# c = [None] * 2
# print(c)
print('\n')

def huffman_tree_cons(freq_dict, org_dict):
    headnum = 0
    container = [None] * 2
    stack = []
    for k in freq_dict:
        for l in freq_dict[k]:
            stack.append(l)
    # print('start stack:',stack)

    res_list = []
    while stack!=[]:
        next_val = None
        comp = True
        combval = 0

        if stack[-1]!='HEAD':
            container[0] = stack.pop(-1)
        else:
            container[0] = None
            stack.pop(-1)
        if stack[-1] != 'HEAD':
            container[1] = stack.pop(-1)
        else:
            container[1] = None
            stack.pop(-1)
        if len(stack) > 0 :
            next_val = stack[-1]
        else:
            comp = False

        if comp:
            if container[0] and container[1]:
                combval = org_dict[container[0]] + org_dict[container[1]]
            else:
                fst_elm = org_dict[container[0]] if container[0] else org_dict["HEAD"]
                snd_elm = org_dict[container[1]] if container[1] else org_dict["HEAD"]
                combval = fst_elm + snd_elm
            #     print(container)
            #     print('fst_elm:{} snd_elm:{}'.format(fst_elm, snd_elm))
            # print('combval:{} next_val:{} next elm:{}'.format(combval, org_dict[next_val], next_val))
            if combval <= org_dict[next_val]:
                stack.append("HEAD")
                headnum += 1
                org_dict["HEAD"] = combval
                # print('org_dict["HEAD"]:', org_dict["HEAD"])
            else:
                tmp_stack = []
                for s in stack[::-1]:
                    val = org_dict[s]
                    if combval > val:
                        tmp_stack.append(stack.pop(-1))
                    else:
                        break
                tmp_stack.append("HEAD")
                headnum += 1
                org_dict["HEAD"] = combval
                # print('tmp stack:', tmp_stack)
                while tmp_stack:
                    stack.append(tmp_stack.pop(-1))
                # print('stack:', stack)

        res_list.append(container)
        container = [None] * 2
        # print("after deal:", stack, '\n')
    return res_list[::-1], headnum

tree_res, treeDepth = huffman_tree_cons(new_res, res)
print('tree res:', tree_res, ' treeDepth:', treeDepth)

def huffman_tree_encode(tree):
    res_dict = {}
    left_path = ""
    right_path = ""
    while tree:
        elm = tree.pop(0)
        if elm[0]:
            left_path += "0"
            res_dict[elm[0]] = left_path
            left_path = right_path
        else:
            left_path += "0"

        if elm[1]:
            right_path += "1"
            res_dict[elm[1]] = right_path
        else:
            right_path += "1"

    return res_dict

path = huffman_tree_encode(tree_res)
print('path:\n', path)

