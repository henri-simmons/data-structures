#Q1

def search_q1(Y, n, x):

    for i in range (0, n):
        if Y[i] == x:
            return i
    return -1


Y = ['apple', 'banana', 'mango', 'grapes', 'pineapple', 'durian']
x = "pineapple"

n = len(Y)
result = search_q1(Y, n, x)
if result == -1:
    print("Element is not present in the list")
else:
    print("Element", x, "is present at index", result)

#answer
'This algorithm has an O(n) time complexity as the time the algorithm takes to finish is relative to the length of the list and there are no loops within loops'

#Q2

def search_q2(X, item):
    first = 0
    last = len(X)-1
    found = False
    while first<=last and not found:
        mid = (first + last)//2
        if X[mid] == item:
            found = True
            print("The element item", item, "was found at index ", X.index(60))
        else:
            if item < X[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


print(search_q2([10, 15, 35, 42, 60, 70, 82, 94], 60))

#answer
'The time complexity of this script is O(log(n)) because on each iteration, the sample space to be searched through is halved when the upper bound or lower bound is redefined.'

#Q3

test = 0
n = 10
for i in range(n):
   test = test + 1

for j in range(n):
   test = test - 1

#answer
'this algorithm runs n times twice because of the two for loops, making it an algorithm with O(n) complexity'

#Q4

i = n
while i > 0:
   k = 2 + 2
   i = i // 2

#answer
'this is an o(log(n)) algorithm as for each repetition of the loop, I is floor divided by 2, bringing it twice as close to reaching 0.'

#Q5

mat = [[1, 2, 3], [1, 1, 1], [5, 7, 8]]
add = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        add += mat[i][j]
print(add)

#answer
'this is an O(n**2) algorithm as each list is iterated through 3 times and there are 3 lists to do this to, making the complecity 3*3, and with n being 3 this is O(n**2)'

#Q6

def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


for n in range(2,12,2):
    print("Series sum for {} is {}".format(n, fibonacci(n)))

#answer
'This function has an exponential time complexity as each call results in two more calls, both of which get called, continually branching out'

