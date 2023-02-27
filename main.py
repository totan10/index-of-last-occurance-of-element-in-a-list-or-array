def lastOcc(l,x):
  low=0
  high=len(l)-1
  while low<=high:
    mid=(low+high)//2
    if l[mid]<x:
      low=mid+1
    elif l[mid]>x:
      high=mid-1
    else:
      if mid==len(l)-1 or l[mid]!=l[mid+1]:
        return mid
      else:
        low=mid+1
  return -1

N=int(input())
arr=input().split()
for i in range(N):
  arr[i]=int(arr[i])
X=int(input())
print(lastOcc( arr, X))