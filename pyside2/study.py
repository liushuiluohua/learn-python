value = {'name': 'Nolan','age': '30'}
print('My name is %(name)s, My age is %(age)s!' % value)
a='Hello'
b='code'
print(a,b)
a,b = b,a
print(a,b)
c='18700953263'
print(list(reversed(c)))
arr={12,45,19,100,78,55,2,11,1000,400,300}
print(sorted(arr))
def quicksort(array):
    less = []
    greater = []
    print(less,greater)
    if len(array) <= 1:
        return array
    print(array)
    pivot =array.pop()          #函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    print(pivot)
    for x in array:
        if x <= pivot:
            less.append(x)      #添加到列表末尾的对象
        else:
            greater.append(x)   #添加到列表末尾的对象 
        print(less,greater)   
    print(less,greater)
    return quicksort(less) + [pivot] + quicksort(greater) #多次重载
array={12,45,19,100,78,55,2,11,1000,400,300}
print(quicksort(array))