# Merge sort is used in python code

def merge_sort(arr, key, decending):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key, decending)
    merge_sort(right, key, decending)

    merge_two_sorted_lists(left, right, arr, key, decending)

def merge_two_sorted_lists(a,b,arr, key, decending):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if not decending:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i+=1
            else:
                arr[k] = b[j]
                j+=1
            k+=1

        else:
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i+=1
            else:
                arr[k] = b[j]
                j+=1
            k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]
    print("The unsorted data is:")
    for element in elements:
        print(element)

    key = 'time_hours'
    merge_sort(arr = elements, key =key, decending=True)
    print(f"Data is sorted by {key}:")
    for element in elements:
        print(element)