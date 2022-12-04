size=int(input('enter the size of list :'))
lst=[]
for i in range(size):
    num=int(input('enter the number :'))
    lst.append(num)
def triple_elem(lst):
    return lst*3
data=list(map(triple_elem,lst))
print(data)

