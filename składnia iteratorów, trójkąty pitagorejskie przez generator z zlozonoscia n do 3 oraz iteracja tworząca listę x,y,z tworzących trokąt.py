#--------------------
x = iter([21,4,'2',[2],(1,2),{1:1},iter([2,1])])
for i in x:
    print(i)
    print(type(i))
    
lista = [1,2,3,4]
z = iter(lista)

#--------------------
def tp(N):
    for x in range(1,N):
        for y in range(1,N):
            for z in range(1,N):
                if x*x+y*y ==z*z:
                    yield(x,y,z)

for i in tp(21):
    print(i)
#--------------------
N = 21
A = ([x for x in range(1,N) for y in range(1,N) for z in range(1,N) if x*x+y*y==z*z])
print(A)
