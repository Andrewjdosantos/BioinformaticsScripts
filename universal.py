import itertools

def k_universal_string(k):
    binary_string = []
    for i in itertools.product([0,1], repeat=k):
        binary_string.append(reduce(lambda a,b: str(a)+str(b), i))

    result = []
    find_k_u_s('', binary_string, k, result)
    print(result)

def find_k_u_s(s, arr, k, r):
    if len(arr) == 0:
        # print s
        r.append(s)
    if not s:
        for s_a in arr:
            arr_left = arr[:]
            arr_left.remove(s_a)
            # print s_a, arr_left
            find_k_u_s(s_a, arr_left, k, r)
    else:
        for i in range(len(arr)):
            if s[-k+1:] == arr[i][:-1]:
                s_a = s + arr[i][-1]
                arr_left = arr[:i] + arr[i+1:]
                # print s_a, arr_left
                find_k_u_s(s_a, arr_left, k, r)


k_universal_string(3)