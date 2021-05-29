import random as rd

def BubbleSort(input_list):
    for i in range(len(input_list)):
        j = 1
        while j < len(input_list) - i:
            if input_list[j - 1] > input_list[j]:
                input_list[j - 1], input_list[j] = input_list[j], input_list[j - 1]
            j += 1
    return input_list


if __name__ == "__main__":
    tar_list = [
        [rd.randint(1, 100) for i in range(20)],
        [rd.randint(1, 100) for i in range(20)],
        [rd.randint(1, 100) for i in range(20)]
    ]

    for i in tar_list:
        print(i)
        output = BubbleSort(i)
        print(output, '\n')