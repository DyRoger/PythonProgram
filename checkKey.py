# Problem Statement
# Check if a key is present in every segment of size k in an array

# !! Start >>>>>>>>>>>
# change j,k,array input according to requirements
# Initialize the array
arr=[]
# Find this // Change this according to input
j=2
# Segement Size 
k=4
# Set an Flag for result calculation
flag=False
print("Enter array elememts :")
for i in range(15):
    #arr.insert(i,int(input()))
    arr.append(int(input()))
print("Array elements are:")
print(arr)
length=len(arr)

# For accessing array elements
l=0
# calculate how many segment will create
if length%k==0:
    length=int(length/k)
else:
    length=int((length/k)+1)
#print(length)
for i in range(length):
    count=0
    while(count<k):
        # l is used here
        if j==arr[l+count]:
            flag=True
            break
        else:
            flag=False
        count += 1
    l=1+(k-1)+l
    if flag==True:
        print("YES")
    else:
        print("NO")