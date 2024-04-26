# implementation of quick sort in python using Lumoto partition scheme

def swap(a, b, arr):
    if a!= b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements, start, end):
    pivot_index = end
    i = start

    for j in range(start, end):
        if elements[j] <= elements[pivot_index]:
            swap(i, j, elements)
            i += 1

    swap(i, end, elements)

    return i


def quick_sort_lumoto(elements, start, end):
    if start >= end or start < 0:
        return

    if start < end:
        p = partition(elements, start, end)

        quick_sort_lumoto(elements, start, p-1)
        quick_sort_lumoto(elements, p+1, end)



if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    print(elements)
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort_lumoto(elements, 0, len(elements)-1)
    print(elements)

    # tests = [
    #     [11,9,29,7,2,15,28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]
    #
    # for elements in tests:
    #     #quick_sort(elements, 0, len(elements)-1)
    #     print(f'sorted array: {elements}')

