#Cache Clearing Assistant by Dave Nissly
#1/28/2025
#v1.1
import csv
import string
import math
data = []
numRows = 0
lastNum = 0
line = []

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: 
        iterations = int(row[1])
        for i in range(iterations):
            s = "/assets/images/products/" + str(row[0]) + '-' + str(i+1) + ".jpg"
            line = []
            line.append(s)
            data.append(line)

    csvfile.seek(0)
    for row in reader: 
        line = []
        iterations = int(row[1])
        for i in range(iterations):
            if i <= 1:
                #first two images need both big and small cloudinary links
                cloudinaryLink1 = "https://media.rallyhouse.com/products/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,w_216,h_308"
                cloudinaryLink2 = "https://media.rallyhouse.com/homepage/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,c_fit,w_730,h_730"
                line = []
                line.append(cloudinaryLink1)
                data.append(line)
                numRows +=1
                if numRows == 20 :
                    blank = []
                    data.append(blank)
                    numRows = 0
                line = []
                line.append(cloudinaryLink2)
                data.append(line)
                numRows+= 1
                if numRows == 20 :
                    blank = []
                    data.append(blank)
                    numRows = 0
                line = []
            else:
                #third image and beyond only need the big cloudinary links
                cloudinaryLink1 = "https://media.rallyhouse.com/homepage/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,c_fit,w_730,h_730"
                line.append(cloudinaryLink1)
                data.append(line)
                numRows += 1
                line = []
                if numRows == 20 :
                    blank = []
                    data.append(blank)
                    numRows = 0
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)