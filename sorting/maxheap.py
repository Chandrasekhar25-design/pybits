def heapify(A, i_e=None):

    i_e = i_e if i_e else len(A)
    
    for i in reversed(range(i_e)):
        max_heap(A, i, i_e)


def max_heap(A, i, i_e=None):

    if not i_e:
        i_e = len(A)

    i_l = 2 * i + 1
    i_r = 2 * i + 2

    if i_l < i_e and A[i] < A[i_l]:
        A[i], A[i_l] = A[i_l], A[i]
        max_heap(A, i_l, i_e)

    if i_r < i_e and A[i] < A[i_r]:
        A[i], A[i_r] = A[i_r], A[i]
        max_heap(A, i_r, i_e)


def sort_heap(A):

    for i in range(len(A)):
        i_e = len(A) - i
        heapify(A, i_e)
        A[0], A[i_e - 1] = A[i_e - 1], A[0]


A = [6, 5, 3, 1, 8, 7, 2, 4]
sort_heap(A)
print A
