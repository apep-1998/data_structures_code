#! /usr/bin/python
"""
    @Author_name : Arsham mohammadi nesyshabori
    @Author_email : arshammoh1998@gmail.com
    @Author_nickname : apep
    @date : 
    @version : 
"""

def bubble_sort(array: list, key=None):
    key = key if key != None else lambda x: x
    array = array.copy()

    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if key(array[i]) > key(array[j]):
                array[i], array[j] = array[j], array[i]

    return array


if __name__ == "__main__":
    import random
    arr = [random.randint(1, 100) for _ in range(100)]
    print("sorted : ", bubble_sort(arr))
    print("arr : ", arr)
    arr = [{"numb":random.randint(1, 100)} for _ in range(100)]
    print("sorted : ", bubble_sort(arr, key=lambda x: x['numb']))
    print("arr : ", arr)
