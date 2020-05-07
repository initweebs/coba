import numpy as np
import math
# perbedaan antara module math dan numpy adalah modul numpy dapat melakukan operasi dengan bilangan kompleks
# sedangkan module math tidak dapat melakukan operasi dengan bilangan kompleks (contoh : 4 j)

a = np.sin (4j) #operasi dengan bilangan kompleks
b = math.sin (90) 
print ("Hasil sin 4j: ",a)
print ("hasil sin 90 dalam radian: ",b)
c = np.degrees (6.283)
print (c)

# perhitungan jarak 2 koordinat kartesian

x1,y1,z1 = 23.7, -9.2, -7.8
x2,y2,z2 = -3.5, 4.8, 8.1

dr = np.sqrt ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print ("perhitungan jarak 2 koordinat kartesian: ",dr)

# menghitung kecepatan bola jatuh
g = 9.8 #in m/s2
h0 = 1.6 #meter
v0 = 14.2 #m/s
t = 2 #s

h = h0 + (v0*t) + (0.5*g*(t**2))
v = v0 - (g*t)
print ("ketinggian bola setelah dilempar selama 2 s: ",h)
print ("kecepatan bola setelah dilempar selama 2 s: ",v)

# menghitung kecepatan
z = 13/3
v_0 = 10
n = 2.5
V = np.sqrt (1-(z/np.sqrt(n**2 + z**2)))
print (V)

#Lists

l1 = [5., "aku", 3+0j, "kambing", 15]
l2 = [1, 2, 3, 4, 5, 6, 7]

l1[0] = l1[0] + 2.5
l1[2] = np.pi
l1[1] = l1[1] + " ganteng"

l2 =l2 + l2
print (l1)
print (l2)

#slicing lists

a= l1 [1:3]
print (a)
print (len(l1))

#Range lists
t =  list (range (10))
print (t)

t1 = list (range (3,10))
print (t1)

t2 = list (range (0,20,2))
print (t2)

#Tuples

t3 = (0,1,3,5,7,8,10,11)
print (t3)

#Multidimensional lists
l3 = [[1,2], [3,4], [5,6]]
print (l3[0][0])
print (l3[0][1])
print (l3[2][0])

#NumpyArray

l4 = list (range (0,10))
u = np.array (l4)
l5 = [0, 1, 3, 4, 6, 8.]
s = np.array (l5)
print (s)

po = np.linspace (0,10,5)
print (po)

ar = np.arange (0, 10 ,2)
print (ar)

#Generating array

i = np.linspace (0,7,8,dtype=float)
print (i)
i2 = np.logspace (0,10,5)
print (i2)

i3 = np.arange (0,20,3)
print (i3)

one = np.ones (5)
print (one)

zero = np.zeros (6)
print (zero)

#Mathematical operation with numpy array
print (i*6)
print (i/2)
print (i-2)
print (np.exp(-i))
print (1+np.exp(-i))

si = 5*np.ones (8)
print (si)

p = np.arange (0,20,2)
p1 = np.arange (0,10,1)
print (p[1:],p[:-1])
print (p1[1:], p1[:-1])
vp = p[1:]-p[:-1]/p1[1:]-p1[:-1]
print (vp)

#boolean indexing

bo = 1 / np.arange (0.5,2,0.25)
print (bo)

print (bo[bo > 1])
print (bo[bo < 1])
# membuat anggota b0 yang lebih dari satu menjadi 1 
bo [bo > 1] = 1
print (bo)
#membuat sebuah array yang ukurannya sama dengan sebuah array yang telah diketahui ukuranny
print (bo.size)
za = np.linspace (0.5,1,bo.size)
print (za)

za [bo == 1] = 1
print (za)

ta = np.sin (np.linspace(0,4*np.pi,9))
print (ta)

ta [np.abs(ta) < 1.e-15] = 0
print (ta)

#multidimensionla array
md =np.array ([[1, 2, 3],[4, 5, 6]])
print (md)

oon = np.ones ((4,4),dtype=float)
print (oon)

# membuat matrix identitas

iden = np.eye (3)
print (iden)

coba = np.arange (6)
print (coba)

coba = np.reshape (coba,(2,3))
print (coba)

#perkalian dot matrix

zz  = np.arange (0,6,1)
zzz = np.arange (10,16,1)
zz  = np.reshape (zz,(2,3))
zzz = np.reshape (zzz,(3,2))
kali = np.dot(zz,zzz)
print (kali)

#dictionaries
#dictionaries dengan membuat nama dan nomor kamar

no = {"ali":202,"zena":402,"Olive":748}
print (no)

#accesing dictionaries
print (no["Olive"])
#dictionaries key shouldn't has string data type
# it can be any immutable python object 
# so it can be integer,string or even tuple.
# but it can't be list, because lists is python mutable object.

weird = {"taxi":53, 56:"texter", "lala":[1,'luka','miku'], "kalimat":'aku ganteng'}

# print key taxi
print (weird["taxi"])

#print key 56
print (weird[56])

#print key lala
print (weird["lala"])

#print key kalimat
print (weird ["kalimat"])

#make a dictionaries from tuple pairs
o = [("clara","Nana"),("jimin","lola"),("porto","rico")]
od = dict (o)
print (o)
#accesing dictionaries elemen
print (od['clara'])

#short introduction about OOP

ui = 'aku suka komputer'

#contoh method yang dapat digunakan pada object dengan tipe data strings adalah split
# untuk penulisannya sendiri adalah 'object.method ()'

print (ui.split())
print (ui.split('m'))

# contoh method untuk object aray 

ni = np.array ([[1,2,3],[7,8,9]])
print (ni)

# menggunakan method 'mean' pada object "ni"
print (ni.mean ())
# contoh penggunaan attribute shape pada numpy array.
print (ni.shape)
print (ni.ndim)
print (ni.std())
