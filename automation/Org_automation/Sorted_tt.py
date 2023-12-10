list1=[10, -8, 2, 4, 6]
list2=[ 4, 16, 36, 64, 100]
list3=[]
j=0
def data(list1):
    if(len(list1)!=0):
        for i in list1:
            list3.append(i)
        print(sorted(list3))

    else:
        print("Input list is empty")
data(list1)