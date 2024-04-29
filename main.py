#task1
def minus(lst):
    return [-y for y in lst]

lst = [1, 2, 3, 4, 5]
print(minus(lst))

#task2
color = input("Choose color: ")
lst = ['blue', 'brown', 'yellow', 'gray']

if color in lst:
    print(lst.index(color))
