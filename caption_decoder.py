from sys import argv
import plistlib


script, filename = argv

#import xml.etree.ElementTree as ET
#tree = ET.parse(filename)
#root = tree.getroot()

pl = plistlib.readPlist(filename)
for image in pl['Images']:
    file_name = image['Image EXIF data']['file_name']
    credit = image['IPTC Fields']['credit']
    caption = image['IPTC Fields']['caption']
    print "%s | %s | %s" % (file_name, credit, caption)
