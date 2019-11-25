# STAT 507 
# 1-1
def is_palindrome(s):
    s = s.lower()
    i = 0
    j = len(s)-1
    while i < len(s) and j < len(s):
        if s[i] == " ":
            i += 1
        if s[j] == " ":
            j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True 

print(is_palindrome('tacocat'))
print(is_palindrome('rats live on no evil star'))
print(is_palindrome('Was it a car or a cat I saw'))
print(is_palindrome('apple'))


# 1-2
def is_abecedarian(s):
    s = s.replace(" ","")
    for i in range(0,len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

print(is_abecedarian('dog'))
print(is_abecedarian('cat'))
print(is_abecedarian('beet'))
print(is_abecedarian('adder'))
print(is_abecedarian('abcd efgh xyz'))



# 1-3
def remove_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_s = ''
    for i in s:
        if i not in vowels:
            new_s = new_s + i
    return new_s

print(remove_vowels('audio'))
print(remove_vowels('cat'))
print(remove_vowels('this is a string'))


# 2-1
def list_reverse(l):
    new_l = []
    if type(l) != list:
        raise TypeError('input not a list')
    else:
        for i in range(-1, -len(l)-1, -1):
            new_l.append(l[i])
    return new_l

print(list_reverse([1,2,3]))
print(list_reverse(['mco', 'jfk', 'dtw']))


# 2-2
def is_sorted(seq):
    for i in range(0, len(seq)):
        if seq[i] <= seq[i+1]:
            return True
        else:
            return False

print(is_sorted('abc'))
print(is_sorted([2,1,0]))
print(is_sorted(('a','b','c')))


# 2-3
def binary_search(t, elmt):
    mid = int((len(t)-1)/2)
    # when case is length 0,1,2
    if len(t) == 0: return False
    elif len(t) == 1:
        if t[0] == elmt: return True
    elif len(t) == 2:
        if t[0] == elmt or t[1] == elmt: return True
    # when case length >= 3
    elif elmt == t[mid]: return True
    elif elmt < t[mid]:
        if elmt in t[0:mid]: return True
    elif elmt > t[mid]:
        if elmt in t[mid:len(t)]: return True
    return False    

print(binary_search([], 7))
print(binary_search([7], 7))
print(binary_search([2,7], 7))
print(binary_search([2,3], 7))
print(binary_search([1,2,4,6], 7))
print(binary_search([1,3,7,9,10], 7))

# 3-1
def char_hist(s):
    s = s.lower()
    dic = {}
    times = 1
    for i in s:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    return dic.items()

print(char_hist("gattaca"))
print(char_hist("!@anna!rttt"))


# 3-2
def bigram_hist(s):
    s = s.lower()
    key = []
    dic = {}
    for i in range(len(s)-1):
        key.append((s[i], s[i+1]))
    for i in key:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    return dic.items()

print(bigram_hist("mississippi"))
print(bigram_hist("cat, dog"))


# 4-1
def check_tuple(t):
    if type(t) != tuple:
        raise TypeeError('input not a tuple')
    for i in t:
        if not (type(i) == int or type(i) == float):
            raise TypeError('input not a float/integer')

def vec_scalar_mult(t,s):
    check_tuple(t)
    if not (type(s) == int or type(s) == float):
        raise TypeError('input not a float/integer')
    a = ()
    for i in t:
        a = a + (i*s,)
    return tuple(a)

print(vec_scalar_mult((1,2,3),3))
print(vec_scalar_mult((1,2.5,3),4.5))


# 4-2
def vec_inner_product(t1, t2):
    check_tuple(t1)
    check_tuple(t2)
    a = 0
    if not (len(t1) == len(t2)):
        raise ValueError('dimensions does not match')
    for (i,j) in zip(t1, t2):
        a = a + i*j
    return a

print(vec_inner_product((1,2,3), (2,3,4)))


# 4-3
def check_valid_mx(my_mx):
    a = len(my_mx[0])
    for i in my_mx:
        if type(i) != tuple:
            return False
        if len(i) != a:
            return False
        for j in i:
            if not (type(j) == float or type(j) == int):
                return False
    return True


print(check_valid_mx(((1,2,3),(1,2,3),(1,2,3))))
print(check_valid_mx(((1,2,3),(1,2,3),(1,2))))
print(check_valid_mx(((1,2,3),(1,2,3),(1,2,'a'))))
print(check_valid_mx(([1,2],(1,2,3),(1,2,3))))


# 4-4
def mx_vec_mult(m,v):
    check_valid_mx(m)
    check_tuple(v)
    vec = ()
    for i in m:
        a = vec_inner_product(i,v)
        vec = vec + (a,)
    return vec

m = ((1,2,3),(1,1,1),(3,2,4))
v = (1,1,1)
mx_vec_mult(m,v)


m = ((1,2,4),(1,1,1),(3,2,4))
v = (1,1,1)
mx_vec_mult(m,v)

# 5-1
def is_valid_sparse_vector(s):
    for i in s:
        if type(i) == float:
            return True
    return False

is_valid_sparse_vector((0.0,1,0.0,1.0))


# 5-2
def sparse_inner_product(d1, d2):
    a = d1.keys()
    b = d2.keys()
    
    for i in a:
        if type(d1[i]) != float:
            raise TypeError("not a valid sparse vector")
    for i in b:
        if type(d2[i]) != float:
            raise TypeError("not a valid sparse vector")
    
    inner = 0
    for i in d1.keys():
        if i in d2.keys():
            inner += d1[i]*d2[i]
    return inner   

d1  = {2:3.0, 5:1.0, 10:2.0}
d2  = {2:4.0, 5:2.0}
sparse_inner_product(d1, d2)


# 6-1
def my_sum(t):
    if len(t) == 0:
        my_sum = 0
    else:
        my_sum = 0
        for i in t:
            my_sum += i
    return my_sum

print(my_sum(()))
print(my_sum((1,2,3)))


# 6-2
def reverse_tuple(t):
    a = ()
    for i in t:
        a = (i,) + a
    return a

print(reverse_tuple((1,2,3)))
print(reverse_tuple((4,7,9)))


# 6-3
def rotate_tuple(t, s):
    if type(t) != tuple:
        raise TypeError('input not a tuple')
    if type(s) != int:
        print('input is a non-integer')
        s = int(s)
    first = t[-s:]
    second = t[:-s]
    return first + second

print(rotate_tuple((1,2,3,4),2))
print(rotate_tuple((1,2,3,4),-1))
print(rotate_tuple((1,2,3,4,5,6,7,8),-3))


