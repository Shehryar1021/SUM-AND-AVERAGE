L=[4,5,1,8,6,10,7,2]
print("ORIGINAL LIST:",L)

count=0
for i in L:
 count+=i

 avg=count/len(L)
 print("SUM=", count)
 print("AVERAGE=", avg)

 L.sort()
 print("SORTED LIST:",L)
 print("SMALLEST ELEMENT IS:",L[0])

print("LARGEST ELEMENT IS:",L[-1])
