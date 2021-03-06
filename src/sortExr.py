def insert_sort(A):
    """сортировка списка А вставками"""
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choice_sort(A):
    """сортировка списка А выбором"""
    for position in range(0, len(A)-1):
        for k in range(position+1, len(A)):
            if A[k] < A[position]:
                A[k], A[position] = A[position], A[k]

def bubble_sort(A):
    """сортировка списка А методом пузырька"""
    for bypass in range(1, len(A)):
        for bubble in range(0, len(A)-bypass):
            if A[bubble] > A[bubble+1]:
                A[bubble], A[bubble+1] = A[bubble+1], A[bubble]

## processing command line input
# returns sorting function by given name
def get_sort_algorithm(name):
    return {
        'bubble': bubble_sort,
        'choice': choice_sort,
        'insert': insert_sort,
    }.get(name)

# check if string parses to an int
def is_parses_to_int(int_string):
    try:
        int(int_string)
    except Exception as e:
        return False
    return True

# divide and process command line args by their meaning
def process_args_list(args_list):
    args_list.pop(0) # first arg is expected to be a file name, so it's popped
    sort_method_name = args_list.pop(0) # second arg is expected to be a sorting name

    # trying to validate the second arg
    if is_parses_to_int(sort_method_name):
        print("First argument should be a sorting method name: insert, choice, bubble")
        return

    algorithm = get_sort_algorithm(sort_method_name)

    # trying to validate given algorithm
    if algorithm is None:
        print("Выберите метод сортировки: insert, choice, bubble")
        return
    else:
        print(algorithm.__doc__)

    # trying to parse the rest of the args to ints
    try:
        list_of_int_args = [int(arg) for arg in args_list]
    except Exception as e:
        print("cannot parse integer")
        return

    # applying algorithms
    algorithm(list_of_int_args)

    print("Sorted list: ", str(list_of_int_args))
    print("Ok")

if __name__ == "__main__":
    process_args_list(sys.argv) # get command line args list and process
