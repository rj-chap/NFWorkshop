import sys
import simplekml

kml = simplekml.Kml()

coordinates = open(sys.argv[1], 'r').read().splitlines()

point_count = 0

for point in coordinates:
	point_count += 1
	kml.newpoint(name="point %i" % point_count, coords=[(tuple(point.split(','))
)])

kml.save("round5.kml")
