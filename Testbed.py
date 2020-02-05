import sys
import subprocess
import time
import io
#s2_out = subprocess.check_output([sys.executable, "test2.py"])
d={}
d[0]=[]
d[1]=[]
d[2]=[]
d[3]=[]
print("Enter the name of Algorithm")
s=input()+'.py'
#print(s)
#s = io.StringIO(s)
start_time=time.time()
for i in range(10):
	exec(open(s).read())
	d[0].append(a[0])
	d[1].append(a[1])
	d[2].append(a[2])
	d[3].append(a[3])
end_time=time.time()
print("Time taken by Setup function is ",sum(d[0])/10)
print("Time taken by Keygen function is ",sum(d[1])/10)
print("Time taken by Encrypt function is ",sum(d[2])/10)
print("Time taken by Decrypt function is ",sum(d[3])/10)
print("Total time taken by ",s," function is ", (end_time-start_time)/10)
#for j in d.keys():
#	print(sum(d[j])/10)
