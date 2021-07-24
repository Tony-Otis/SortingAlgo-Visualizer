def insertion_sort(array):

    for i in range(1, len(array)):

        key = array[i]

        j = i - 1

        while j >= 0 and key < array[j]:

            array[j + 1] = array[j]
            j -= 1

            yield array

        array[j + 1] = key


        yield array