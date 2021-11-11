file_input = open('antiqs.in', 'r')
file_output = open('antiqs.out', 'w')

n = int(file_input.readline())
arr = [x for x in range(1,n + 1)]
for i in range(2,n):
    arr[i], arr[i // 2] = arr[i // 2], arr[i]
print(*arr, file = file_output)
file_output.close() 
##import random
##def qsort(left,right,arr):
##    pivo=arr[(left+right)//2]
##    i=left
##    j=right
##    cnt=0
##    print(*arr,' p>', pivo)
##    while i<=j:
##        while arr[i]<pivo:
##            i+=1
##            cnt+=1
##        while pivo<arr[j]:
##            j-=1
##            cnt+=1
##        if i<=j:
##            arr[i],arr[j]=arr[j],arr[i]
##            i+=1
##            j-=1
##    print(*arr,' p>', pivo, ' >',cnt)
##    if left<j: qsort(left,j,arr)
##    if i<right: qsort(i,right,arr)

#arr = [random.randrange(1, 10, 1) for i in range(10)]
#qsort(0, len(arr) - 1, arr)
#print(*arr)

