#! /usr/bin/python
"""
    @Author_name : Arsham mohammadi nesyshabori
    @Author_email : arshammoh1998@gmail.com
    @Author_nickname : apep
    @date : 
    @version : 
"""

def _merge(array, start, middel, end, key):
    out = []
    i = start
    j = middel+1
    while i <= middel and j <= end:
        if key(array[i]) < key(array[j]):
            out.append(array[i])
            i+=1
        else:
            out.append(array[j])
            j+=1

    while i <= middel:
        out.append(array[i])
        i+=1

    while j < end:
        out.append(array[j])
        j+=1

    array[start:start+len(out)] = out


def _merge_sort(array, start, end, key):
    if start < end:
        middel = (start+end) // 2
        _merge_sort(array, start, middel, key)
        _merge_sort(array, middel+1, end, key)
        _merge(array, start, middel, end, key)

def merge_sort(array: list, key=None):
    key = key if key is not None else lambda x: x
    array = array.copy()
    _merge_sort(array, 0, len(array)-1, key)
    return array


if __name__ == "__main__":
    import random
    arr = [3, 4, 5 ,1 ,3 ,5 ,6, 9, 7, 3, 7, 8]
    print("sorted : ", merge_sort(arr))
    print("arr : ", arr)
    arr = [{"numb":random.randint(1, 100)} for _ in range(100)]
    print("sorted : ", merge_sort(arr, key=lambda x: x['numb']))
    print("arr : ", arr)



