#Cache Clearing Assistant by Dave Nissly
#1/28/2025
#v1.1
import csv
import string
import math

#data holds the netuite resources
data = []
#data2 holds the cloudinary resources
data2 = []
#numRows is used to keep track of when to skip a line for cloudinary
numRows = 0
#line holds temporary row data
line = []

#open the file as csvfile
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    #iterate through and generate netsuite resources for each product
    #count of resources is equal to the number of images for each product
    for row in reader: 
        iterations = int(row[1])
        for i in range(iterations):
            s = "/assets/images/products/" + str(row[0]) + '-' + str(i+1) + ".jpg"
            line = []
            line.append(s)
            data.append(line)
        line = []
        for i in range(iterations):
            if i <= 1:
                #first two images need both big and small cloudinary links
                cloudinaryLink1 = "https://media.rallyhouse.com/products/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,w_216,h_308"
                cloudinaryLink2 = "https://media.rallyhouse.com/homepage/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,c_fit,w_730,h_730"
                line = []
                line.append(cloudinaryLink1)
                data2.append(line)
                numRows +=1
                if numRows == 20 :
                    blank = []
                    data2.append(blank)
                    numRows = 0
                line = []
                line.append(cloudinaryLink2)
                data2.append(line)
                numRows+= 1
                if numRows == 20 :
                    blank = []
                    data2.append(blank)
                    numRows = 0
                line = []
            else:
                #third image and beyond only need the big cloudinary links
                cloudinaryLink1 = "https://media.rallyhouse.com/homepage/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,c_fit,w_730,h_730"
                line.append(cloudinaryLink1)
                data2.append(line)
                numRows += 1
                line = []
                if numRows == 20 :
                    blank = []
                    data2.append(blank)
                    numRows = 0

#write the data into the output file        
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
    writer.writerows(data2)