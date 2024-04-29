# Selection sort of order O(N^2)
def selection_sort(arr, list):
    size = len(arr)
    size_list = len(list)
    for k in range (size_list):
        for i in range(size-1):
            min_index = i
            for j in range(min_index+1,size):
                if arr[j][list[k]] < arr[min_index][list[k]]:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    print('Given unsorted array:', *elements, sep='\n')

    list = ['First Name','Last Name']
    selection_sort(elements, list)

    print('Sorted array:', *elements, sep='\n')