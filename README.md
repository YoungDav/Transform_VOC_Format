### This tools help you to transfrom annotation format to VOC2007 format used for py-faster-rcnn

ANNOTATION FORMAT:  
{  
&emsp;img_name_2 : [ [xmin_1, ymin_1, xmax_1, ymax_1, label_1], [xmin_2, ymin_2, xmax_2, ymax_2, label_2] .... ],  
&emsp;img_name_3 : [ [xmin_1, ymin_1, xmax_1, ymax_1, label_1], [xmin_2, ymin_2, xmax_2, ymax_2, label_2] .... ],
  ....  
}

case:  
{  
&emsp;'00002.jpg' : [ [  21,  48,  99, 76, 'cat'], [ 22,  21,  34,  78, 'dog'] .... ],  
&emsp;'00003.jpg' : [ [  19,  87,  78, 99, 'dog'], [ 32,  76,  90,  12, 'cat'] .... ],
&emsp;....  
}

Transfrom VOC Format

00002.jpg -> 00002.xml
