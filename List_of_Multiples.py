def list_of_multiples (num, length):
    t=[]
    for i in range(length):
        t.append((i+1)*num)
    return t
print(list_of_multiples(7,5))

