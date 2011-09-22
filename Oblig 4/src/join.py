


def join(delimter, *rest):
    a = []
    for arg in rest:  
        if type(arg) == tuple:
            a.extend(list(arg))
        elif type(arg) == list:
            a.extend(arg)
        else:
            a.append(arg)
    return delimter.join(a)


list1 = ['s1', 's2', 's3']
tuple1 = ('s4', 's5')

ex1 = join(' ', 't1', 't2', list1, tuple1, 't3', 't4')
ex2 = join(' # ', list1, 't0')
print ex1
print ex2