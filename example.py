
'''====bytes conversion===='''

print(hex(52))#0x34
print(oct(22))#0o26
print(bin(36))#0b100100
print(0xac) #172
print(0o36) #30
# print(0b1011)#11
print(0o254)#172
print(0b10101100)#172
a=0xac
b=bin(a)
print(b)#0b10101100
b=oct(a)
print(b)#0o254
b=hex(a)
print(b)#0xac 
a=(10,20,3,5)
c=[1,2,3,8]
d={1,2,3,8}
b=bytes(a)
print(b,type(b))#b'\n\x14\x03\x05' <class 'bytes'>

print(b[0])
a=(1,2,300,5)
b=bytes(a)
print(b) #ValueError: bytes must be in range(0, 256)
a=(-1,2,30,5)
b=bytes(a)
print(b) #ValueError: bytes must be in range(0, 256)
print(id(a))


'''===nested slicing===='''
a=[1,2,'guido vann rossum',['a','python','nestedlist',3],1+5j,[4,5,6]]

print(type(a))             #<class 'list'>
print(a.index('python'))   #ValueError: 'python' is not in list
print(a[2])                #guido vann rossum
print(a[3][2])             #nestedlist
print(a[3][2][2:])         #stedlist
print(a[4])                #(1+5j)
print(a[2][2])             #i
print(a[-1][-1])           #6
print(a[-3][::-1])         #[3, 'nestedlist', 'python', 'a']
print(a[::-1])             #[[4, 5, 6], (1+5j), ['a', 'python', 'nestedlist', 3], 'guido vann rossum', 2, 1]
print(a[::-2])             #[[4, 5, 6], ['a', 'python', 'nestedlist', 3], 2]
print(a[::-3])             #[[4, 5, 6], 'guido vann rossum']
print(a[::-4])             #[[4, 5, 6], 2]
print(a[::-5])             #[[4, 5, 6], 1]
print(a[::-6])             #[[4, 5, 6]]
print(a[::-7])             #[[4, 5, 6]]
print(a[2][::-1])            #mussor nnav odiug
a.append(1989)
print(a)                    #[1, 2, 'guido vann rossum', ['a', 'python', 'nestedlist', 3], (1+5j), [4, 5, 6], 1989]
a.append(3)
print(a)                   #[1, 2, 'guido vann rossum', ['a', 'python', 'nestedlist', 3], (1+5j), [4, 5, 6], 3]
a.insert(-1,2008)
print(a)                    #[1, 2, 'guido vann rossum', ['a', 'python', 'nestedlist', 3], (1+5j), [4, 5, 6],2008,3]
print(a.pop(-2))            #2008
print(a.pop())              #3

a=[58,796,258,753,155,12,1]
b=['int','float','str','TUPLE','SET','DICT','BYTES','BYTE ARRAY','FROZEN SET','COMPLEX']
a.sort()
b.sort()
print(b)#['BYTE ARRAY', 'BYTES', 'COMPLEX', 'DICT', 'FROZEN SET', 'SET', 'TUPLE', 'float', 'int', 'str']
print(a)#[1, 12, 58, 155, 258, 753, 796]
a.sort(reverse=True)
b.sort(reverse=True)
print(a)#[796, 753, 258, 155, 58, 12, 1]
print(b)#['str', 'int', 'float', 'TUPLE', 'SET', 'FROZEN SET', 'DICT', 'COMPLEX', 'BYTES', 'BYTE ARRAY']


'''is and is not gives the True or False
-->is represents that id ID's of the two variables are same it gives TRUE else FALSE
--> is not gives that ID's of two variables are different gives TRUE else FALSE
'''
a=12
b=13
c=13
print(id(a),id(b),id(c))  #2586640515664 2586640515696 2586640515696
print(a is not b)  #True 
print(a is  b)      #False



