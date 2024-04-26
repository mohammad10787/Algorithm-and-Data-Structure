# Insertion sort is not good for big data. We preferably use it for smaller data
import statistics


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor

def running_median(elements):
    insertion_sort(elements)

    return statistics.median(elements)



if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    #
    for i in range (0, len(elements)):
        print(f'Running Median:', running_median(elements[0:i+1]))