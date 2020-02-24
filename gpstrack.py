import csv
from gmplot import gmplot


gmap=gmplot.GoogleMapPlotter(28.689169,77.324448,17)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"

with open("route.csv",'r') as f:
    reader=csv.header(f)
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        print(lat)
        print(long)
        print(lat+long)

        if k==0:
            gmap.marker(lat,long,'yellow')
        else:
            gmap.marker(lat,long,'blue')
gmap.marker(lat,long,'red')
gmap.draw("mymap.html")
