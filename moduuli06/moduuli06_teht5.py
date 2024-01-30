def odd_num_remover(list_of_nums):
    list_without_odd = []
    for num in list_of_nums:
        if num % 2 == 0:
            list_without_odd.append(num)
    return list_without_odd

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000000, 1000001]
    print(odd_num_remover(test_list))