def Hansu(n):
  numbers = list(map(int,list(str(n))))
  degree=[]
  for i in range(len(numbers)-1):
    degree.append(numbers[i]-numbers[i+1])
  if min(degree)==max(degree): return True
  else: return False
n=int(input())
if n<100:
  cnt=n
else:
  cnt=99
  for x in range(100,n+1):
    ret = Hansu(x)
    if ret: cnt +=1
print(cnt)