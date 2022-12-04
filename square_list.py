size=int(input('enter the size of list :'))
lst=[]
for i in range(size):
    num=int(input('enter the number :'))
    lst.append(num)
def square_elem(lst):
    return lst**2
data=list(map(square_elem,lst))
print(data)

