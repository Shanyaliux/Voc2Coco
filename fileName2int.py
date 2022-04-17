import os
import xml.etree.cElementTree as ET

ROOT_PATH = '/home/lgh/PycharmProjects/Voc2Coco/NEU-DET'

xmlDir = os.path.join(ROOT_PATH, 'xml/')
imgDir = os.path.join(ROOT_PATH, 'img/')

xmlList = os.listdir(xmlDir)
for i, xml in enumerate(xmlList):
    (name, ex) = os.path.splitext(xml)
    tree = ET.parse(xmlDir + xml)
    root = tree.getroot()
    newName = ("%05d" % (i + 1))
    root.find('filename').text = newName + '.jpg'
    tree.write(xmlDir + xml)
    os.rename(xmlDir + xml, xmlDir + newName + ex)
    os.rename(imgDir + name + '.jpg', imgDir + newName + '.jpg')
    print(name + '  -->  ' + newName)


