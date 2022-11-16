import re

def wordcount(string):
    s=re.split('\.|,| ',string)

    res = []
    for val in s:
        if val != '':
            res.append(val)

    unique=(list(set(res)))

    count=[]
    for i in range(len(unique)):
        count.append(str(unique[i])+"="+str(s.count(unique[i])))

    return print(', '.join(count))

string=input("Enter your string: ")

wordcount(string)






