T=int(input())
for i in range(T):
  n=int(input())
  a=list(map(int,input().split()))
  d1=[(a[i]-(i+1)) for i in range(len(a))]
  a1=[chr(i) for i in range(97,97+len(a))]
  a2=[0]*len(a1)
  r=[chr(i) for i in range(97,97+len(a))]
  j=0
  count=0    
  while j==0:
    for i in range(len(a1)):
      a2[i+d1[i]]=a1[i]
    count+=1 
    if a2==r:
      j=1
    else:
      for i in range(len(a1)):
        a1[i]=a2[i]    
  print(count)
    