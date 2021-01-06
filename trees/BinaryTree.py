tree = [None] * 10

def set_root(key):
    if tree[0]:
        print("Root already exist.")
    else:
        tree[0] = key

def set_left(key, parent):
    if tree[parent]:
        tree[2 * parent + 1] = key
    else:
        print("Parent does not exist, please check.")

def set_right(key, parent):
    if tree[parent]:
        tree[2 * parent + 2] = key
    else:
        print("Parent does not exist, please check.")

def print_tree():
    for i in range(10):
        if tree[i]:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()

set_root("A")
set_left("B", 0)
set_right("C", 0)
set_left("D", 1)
set_right("E", 1)
set_left("F", 2)
set_right("G", 2)
print_tree()