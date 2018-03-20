#coding:utf-8
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import cv2
import os
import json

def out_xml(root, path):
    rough_string = ET.tostring(root, 'utf-8')
    reared_content = minidom.parseString(rough_string)
    with open(path, 'w') as fs:
        reared_content.writexml(fs, addindent="\t", newl="\n")
    return True


def dict_to_xml(key, value, datadir, xml_path):

    # 0. annotation
    annotation_ = ET.Element('annotation')

    # 1. folder
    folder_ = ET.SubElement(annotation_, 'folder')
    folder_.text = 'datadir'

    file_name = key.split('/')[-1]

    # 2. filename
    if file_name.split('.')[-1] in ['jpg']:

        file_name_ = ET.SubElement(annotation_, 'filename')
        file_name_.text = file_name

    else:
        print "{} is error file format".format(file_name)
        return 0


    # 3. size
    img = cv2.imread(os.path.join(datadir, file_name))
    size_ = ET.SubElement(annotation_, 'size')
    width_ = ET.SubElement(size_, 'width')
    width_.text = str(img.shape[1])
    height_ = ET.SubElement(size_, 'height')
    height_.text = str(img.shape[0])
    depth_ = ET.SubElement(size_, 'depth')
    depth_.text = str(img.shape[2])

    # 4. segmented
    segmented_ = ET.SubElement(annotation_, 'segmented')
    segmented_.text = '0'


    # 5. object
    for obj in value:
        xmin, ymin, xmax, ymax, label = obj
        object_ = ET.SubElement(annotation_, 'object')

        name_ = ET.SubElement(object_, 'name')
        name_.text = label

        pose_ = ET.SubElement(object_, 'pose')
        pose_.text = 'Frontal'

        truncated_ = ET.SubElement(object_, 'truncated')
        truncated_.text = '1'

        difficult_ = ET.SubElement(object_, 'difficult')
        difficult_.text = '0'

        bndbox_ = ET.SubElement(object_, 'bndbox')
        xmin_ = ET.SubElement(bndbox_, 'xmin')
        xmin_.text = str(xmin)
        ymin_ = ET.SubElement(bndbox_, 'ymin')
        ymin_.text = str(ymin)
        xmax_ = ET.SubElement(bndbox_, 'xmax')
        xmax_.text = str(xmax)
        ymax_ = ET.SubElement(bndbox_, 'ymax')
        ymax_.text = str(ymax)

    out_xml(annotation_, xml_path)

dict_to_xml('detection_test.jpg', [[1,2,3,4,'pn']], '../data', 'test.xml')

def main():
    datadir = 'PATH OF IMGDIR'
    json_path = 'PATH SAVE ANNOTATION'
    xml_dir = 'PATH SAVE OUTPUT XML'

    json_ = json.loads(open(json_path).read())

    for key in json_.keys():
        xml_name = key.split('/')[-1].split('.')[0] + '.xml'
        xml_path = os.path.join(xml_dir, xml_name)
        value = json_[key]
        dict_to_xml(key, value, datadir, xml_path)

def test():
    dict_to_xml('xiaohuangren.jpg', [[10, 20, 40, 50, 'person'], [10, 20, 40, 50, 'person']], 'VOC2018', 'xiaohuangren.xml')

if __name__ == '__main__':
    test()