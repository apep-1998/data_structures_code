#! /usr/bin/python
"""
    @Author_name : Arsham mohammadi nesyshabori
    @Author_email : arshammoh1998@gmail.com
    @Author_nickname : apep
    @date : 
    @version : 
"""

def insertion_sort(array: list, key=None):
    key = key if key != None else lambda x: x
    array = array.copy()

    for k in range(1, len(array)):
        item = array[k]
        i = k
        while i >= 1 and key(array[i-1]) > key(item):
            array[i] = array[i-1]
            i-=1
        array[i] = item

    return array


if __name__ == "__main__":
    test_arr = [5, 2, 5, 3, 5, 3]
    print("sorted : ", insertion_sort(test_arr))
    print("list: ", test_arr)

    test_arr = [{"s": 5}, {"s": 3}, {"s": 4}, {"s": 2}, {"s": 2}]
    print("sorted : ", insertion_sort(test_arr, key=lambda x: x['s']))
    print("list: ", test_arr)
