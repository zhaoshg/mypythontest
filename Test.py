import sort
import recursion

if __name__ == '__main__':
    arr = [3, 1, 5, 2, 4, 7, 8, 98, 32, 12, 34, 56, 27, 18, 21, 25, 43]
    print(sort.shell_sort(arr[:]))
    print(sort.simple_sort(arr[:]))
    print(sort.insert_sort(arr[:]))
    print(recursion.sumarr(arr[:]))
    print(recursion.countarr(arr[:]))
    print(recursion.findmax(arr[:]))
