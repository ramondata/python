import gc
import subprocess

#cl = subprocess.Popen("$?", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#out, err = cl.communicate()
#print(out)
#print(err)

x = 0

for i in range(1000):
    x += i
x = []


for i in range(10000):
    x.append(x)

cl = gc.collect()
print(cl)