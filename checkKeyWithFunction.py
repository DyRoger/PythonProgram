# Problem Statement
# Check if a key is present in every segment of size k in an array

def function(arr1,seg,element,len):
    # Set an Flag for result calculation
    flag=False
    # print(arr)
    # print(seg)
    # print(element)
    # print(len)
    l=0
    # calculate how many segment will create
    if len%seg==0:
        len=int(len/seg)
    else:
        len=int((len/seg)+1)
    for i in range(len):
        count=0
        while(count<seg):
            # l is used here
            if element==arr1[l+count]:
                flag=True
                break
            else:
                flag=False
            count += 1
        l=1+(seg-1)+l
    if flag==True:
        print("YES")
    else:
        print("NO")
# Initialize the array
arr=[]
print("Enter array elememts :")
for i in range(9):
    #arr.insert(i,int(input()))
    arr.append(int(input()))
print("Array elements are:")
print(arr)
# Which element to find
j=int(input("Enter the Element want to find :"))
# Segement Size 
k=int(input("Enter the segment no to divide :"))

length=len(arr)
function(arr,k,j,length)

