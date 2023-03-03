import time

print(time.time()/(60*60*24*7*52))

def prod():
# Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


starttime = time.time()
result = prod()
endtime = time.time()

print('result is '+str(len(str(result)))+' long and took '+str(endtime-starttime)+'seconds')

# using time.sleep()