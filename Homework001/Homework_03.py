def solution(string):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    count = 0
    for alphabet in string:
        if vowels.count(alphabet) > 0:
            count = count + 1

    print("Number of vowels = ", count)


entry = input("Enter the string : ")

solution(entry)
