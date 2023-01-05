import numpy as np
import numpy as np
import matplotlib.pyplot as plt

#Pie and Bar charts are drawn for question 01 and Question 06

print("====== Question 01 ========")

original = np.arange(10, 49)
print("Original array:")
print(original)
print("Reverse array:")
reverse = original[::-1]
print(reverse)

plt.bar(original, reverse) #Bar Chart representing the relationship between original array and its revrese
plt.show()

plt.pie(original) #Pie Chart representing the distribution of elements in Oroginal array
plt.show()

print("====== Question 02 ========")

a = np.random.random((5, 5))
print("Original Array:")
print(a)
amin, amax = a.min(), a.max()
print("Minimum and Maximum Values:")
print(amin, amax)

print("====== Question 03 ========")

anorm = (a - amin) / (amax - amin)
print("After normalization:")
print(anorm)

print("====== Question 04 ========")

x = np.random.random((5, 3))
print("5x3 array:")
print(x)
y = np.random.random((3, 2))
print("3x2 array:")
print(y)
z = np.dot(x, y)
print("Dot product of two arrays:")
print(z)

print("====== Question 05 ========")

yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')  # subtract one day from today
print("Yestraday: ", yesterday)
today = np.datetime64('today', 'D')
print("Today: ", today)
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')  # add one day to today
print("Tomorrow: ", tomorrow)

print("====== Question 06 ========")

x = np.random.uniform(0, 10, 10)
print(x)
print('Random Array:\n', x)

y=x.astype(int)

print("method 1:", x.astype(int))
print("method 2:", x - x % 1)
print("method 3:", np.ceil(x) - 1)
print("method 4:", np.trunc(x))
print("method 5:", np.floor(x))

plt.bar(x, y) #Bar Chart representing the relationship between x array and y revrese
plt.show()

plt.pie(y) #Pie Chart representing the distribution of elements in integers of random array
plt.show()

print("====== Question 07 ========")

x = np.zeros(10, [('position', [('x', float, (1,)),
                                ('y', float, (1,))]),
                  ('color', [('r', float, (1,)),
                             ('g', float, (1,)),
                             ('b', float, (1,))])])
print(x)
