# # code your iterative algorithm here
def binary_search(lst, target):
    first = 0
    last = len(lst) - 1
    found = False
    lst.sort()
    iterations = 1

    while first <= last and not found:
        mid = (first + last) // 2
        print(f"Iterations: {iterations}")

        if lst[mid] == target:
            found = True
        else: 
            if target < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
            iterations += 1
    
    return found

def binary_recurs(lst, target):
    print(lst)
    if len(lst) == 0:
        return False

    else: 
        mid = len(lst) // 2

        if lst[mid] == target:
            return True
        else:
            if target < lst[mid]:
                return binary_recurs(lst[:mid], target)
            else: 
                return binary_recurs(lst[mid+1:], target)

if __name__ == '__main__':
    # test_list = [1, 2, 3, 4, 5, 6, 7]
    test_list = [1, 2, 3, 44, 51, 16, 71]
    test_list.sort()
    print(binary_recurs(test_list, 16))