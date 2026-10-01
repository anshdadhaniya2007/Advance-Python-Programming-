import numpy as np
arr=np.arange(1,11)
print('original arr :',arr)
print('first 5 elements :',arr[:5])
print('elements from 3 to 7 :',arr[2:7])
print('every 2nd elements :',arr[::2])
print('reverse arr :',arr[::-1])
print('sum :',np.sum(arr))
print('mean :',np.mean(arr))
print('median :',np.median(arr))
print('maximum :',np.max(arr))
print('minimum :',np.min(arr))
arr1=arr+5
print('after adding 5 to every element :',arr1)
arr2=arr*10
print('after multiplying 10 to every element :',arr2)