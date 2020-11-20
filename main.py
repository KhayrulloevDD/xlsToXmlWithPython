import xlrd
path = "exportlocation.xls"
fileData = xlrd.open_workbook(path)
inputWorkSheet = fileData.sheet_by_index(0)
xmlString = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Branches xmlns:datatype="http://datatype.fc.ofss.com" xmlns:validationdtoapp="http://validation.dto.app.fc.ofss.com" xmlns:dtocommondomainframework="http://dto.common.domain.framework.fc.ofss.com" xmlns:ns4="http://enumeration.fc.ofss.com">
        """
for i in range(1, inputWorkSheet.nrows):
    branchCode = str(inputWorkSheet.cell_value(i, 2))
    latitude = str(inputWorkSheet.cell_value(i, 3))
    longitude = str(inputWorkSheet.cell_value(i, 4))
    xmlString += """<Branch>
        <coordinates>
            <latitude>""" + latitude + """</latitude>
            <longitude>""" + longitude + """</longitude>
        </coordinates>
        <ID>""" + branchCode + """</ID>
        <name>Orienbank</name>
        <PostalAddress>
            <datatype:city>Tajikistan</datatype:city>
            <datatype:country>Tajikistan</datatype:country>
            <datatype:line1>101</datatype:line1>
            <datatype:line2>101</datatype:line2>
        </PostalAddress>
        <Services>
            <id>7</id>
        </Services>
        <type>BRANCH</type>
        <phone>
            <number>2222</number>
        </phone>
        <workDays>Mon-Fri</workDays>
        <Timings>08:00-17:00</Timings>
    </Branch>"""
xmlString += "\n</Branches>"
with open("Output.txt", "w") as xmlFile:
    xmlFile.write(xmlString)
print(xmlString)