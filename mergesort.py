# merge_sort in Python


def merge_sort(array):
    if len(array) <= 1:

        return
    #  r is the point where the array is divided into two subarrays
    r = len(array)//2
    L = array[:r]
    M = array[r:]

    # Sort the two halves
    merge_sort(L)
    merge_sort(M)

    i = j = k = 0

    # Until we reach either end of either L or M, pick larger among
    # elements L and M and place them in the correct position at A[p..r]
    while i < len(L) and j < len(M):
        if L[i] < M[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = M[j]
            j += 1
        k += 1


    # When we run out of elements in either L or M,
    # pick up the remaining elements and put in A[p..r]
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1

        yield array

    while j < len(M):
        array[k] = M[j]
        j += 1
        k += 1

    yield array
# Print the array
# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()


# # Driver program
# if __name__ == '__main__':
#     array = [6, 5, 12, 10, 9, 1]

#     merge_sort(array)

#     print("Sorted array is: ")
#     printList(array)