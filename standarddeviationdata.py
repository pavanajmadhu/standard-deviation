import csv
import math

with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data) :
    n=len(data)
    total=0

    for i in data:
        total+=int(i)

    mean=total/n

    return(mean)

#subracting mean from data points and squaring

squared_list=[]

for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

#getting sum

sum=0

for  i in squared_list:
    sum=sum+i

#dividing the sum by (total values-1)

result=sum/(len(data)-1)

#getting square root
standarddeviation=math.sqrt(result)

print("standard deviation = ",standarddeviation)