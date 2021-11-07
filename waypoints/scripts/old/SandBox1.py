FILE = "/home/hk/catkin_ws/src/waypoints/scripts/file.csv"

coordinateCount = 0

f = file (FILE,"r")
rawCoordinates = f.readlines()
f.close()
coordinates=[]
for i in rawCoordinates:
	#print i
	coordinates.append([float(i.split(",")[0]), float(i.split(",")[1])])

print coordinates
coordinateCount = len(coordinates)
print coordinateCount
