#Cache Clearing Assistant by Dave Nissly
#1/28/2025
#v1.0
import csv
import string
import math

data = []
header = ["Name", "# Images", "Cache Assets"]
data.append(header)
numRows = 0
lastNum = 0

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    #iterate over rows
    for row in reader:  # Each row is a list named line
        line = []
        #row[2] contains the number of images on that item
        iterations = int(row[1])
        #if the number of images is changing, places a header row that describes the change and reset the 20 line skip counter
        if lastNum != iterations:
            message = "Items with " + str(iterations) + " images"
            line.append(message)
            data.append(line)
            lastNum = iterations
            numRows = 0
            line = []
        #add name/sku [0], and # of images [1] to the row
        #line.append(row[0]) (uncomment to re-enable internal id tracking)
        line.append(row[0])
        line.append(iterations)
        #iterate through as many times as there are images
        for i in range(iterations):
            s = "/assets/images/products/" + str(row[0]) + '-' + str(i+1) + ".jpg"
            line.append(s)
        #iterate through this process as many times as there are images per item
        for i in range(iterations):
            if i < 2:
                #first two images need both big and small cloudinary links
                cloudinaryLink1 = "https://media.rallyhouse.com/products/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,w_216,h_308"
                cloudinaryLink2 = "https://media.rallyhouse.com/homepage/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,c_fit,w_730,h_730"
                line.append(cloudinaryLink1)
                line.append(cloudinaryLink2)
            else:
                #third image and beyond only need the big cloudinary links
                cloudinaryLink1 = "https://media.rallyhouse.com/homepage/" + row[0] + "-" + str(i+1) + ".jpg?tx=f_auto,c_fit,w_730,h_730"
                line.append(cloudinaryLink1)
        data.append(line)
        numRows += 1
        
        #comment out when we can import more than 20
        if numRows % 20 == 0 :
            blank = []
            data.append(blank)

with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)



