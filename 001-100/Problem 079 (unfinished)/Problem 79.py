                                                   #79 (unfinished)

#x is a list
def f(x):
    list1 = list(str(x[0]))
    i = 1
    while i < len(x):
        y = list(str(x[i]))
        a = y[0]
        if a in list1:
            list_a = list1[1 + list1.index(a):len(list1)] #list of elements after a
        b = y[1]
        if b in list1:
            list_b = list1[1 + list1.index(b):len(list1)] #list of elements after b
        c = y[2]
        if a in list1: #check if the first digit of the new number (abc) is in the list
            if b in list_a : # if a is in list, check for numbers after a whether b is in list
                if c in list_b: # if both a and b are in list in that order, check if c in list after b
                    i += 1
                else: # if a and b are in list (as explained above) but c is not in list for numbers after b then add c to the back
                    list1.append(y[-1])
                    i += 1
            elif c in list_a: # if a and c are in list in that order, but b not in list, insert it right before c
                z1 = list1.index(c)
                list1.insert(z1,b)
                i+=1
            else: # if a in list but b and c are not on those after a, add bc to the end of the list
                del y[0]
                list1 += y
                i += 1
        elif b in list1: #if a not in list check whether b in list
            if c in list_b: #if b in list but not a, check whether c in list after b
                z0 = list1.index(b)
                list1.insert(z0,a) # if b and c in list in that order but a not in list, add it before b
                i+=1
            else: #a not in list and c not in list after b, we add c after b and a before b:
                z1 = list1.index(b)
                list1.insert(z1+1,c) #we insert c after b
                list1.insert(z1,a) #and a before b
                i+=1
        elif c in list1: #if only c is on the list, then add the first two before the appearance of the third on the list
            z2 = list1.index(c)
            list1.insert(z2,b)
            list1.insert(z2,a)
            i+=1
        else: #if no digits are on the list, then add the new number to the back of the list
            list1 += y
            i += 1
    return "".join(list1)
