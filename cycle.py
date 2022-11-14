import time

i=0
k=0
j=0
z=0
f=open('ww.txt','r+') 
a=""
print(time.perf_counter())
for i in range(10000):
    for j in range(10000):
        z+=1
        
    
a=str(z)+' итераций пройдено, '+str(time.perf_counter())+' секунд прошло \n'
f.write(a)
print (a)

f.close()
print ('vse')