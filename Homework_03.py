def solution(str):
    vowels = ("a","e","i","o","u","A","E","I","O","U")
    count = 0
    for alphabet in str:
        if vowels.count(alphabet) > 0:
            count = count + 1

    print("Number of vowels = ", count)


str = input("Enter the string : ")

solution(str)