import xml.etree.ElementTree as ET
import csv
import datetime

tree = ET.parse("yieldcurve.xml")
root = tree.getroot()
out = open('yieldcurve.csv', 'w', newline='')

csvwriter = csv.writer(out)
first = True

start = datetime.date(2019, 10, 1)
end = datetime.date(2019, 12, 1)

for member in root.iter('{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties'):
  date = datetime.datetime.strptime(member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}NEW_DATE").text, "%Y-%m-%dT%H:%M:%S").date()
  
  if ((start <= date) and (date <= end)):
  
    if first:
      csvwriter.writerow(['date', '2 yr', '3 yr', '5 yr', '7 yr', '10 yr', '30 yr'])
      first = False

    csvwriter.writerow([
            member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}NEW_DATE").text,
            member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}BC_2YEAR").text,
            member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}BC_3YEAR").text,
            member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}BC_5YEAR").text,
            member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}BC_7YEAR").text,
            member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}BC_10YEAR").text,
            member.find("{http://schemas.microsoft.com/ado/2007/08/dataservices}BC_30YEAR").text,
                        ])
out.close()