# code your iterative algorithm here
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

if __name__ == '__main__':
    # test_list = [1, 2, 3, 4, 5, 6, 7]
    test_list = [1, 2, 3, 44, 51, 16, 71]
    print(binary_search(test_list, 3))
