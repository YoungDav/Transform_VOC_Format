# Transform_VOC_Format

ANNOTATION FORMAT:
{  
&emsp;img_name_1 : [ [xmin_1, ymin_1, xmax_1, ymax_1, label_1], [xmin_2, ymin_2, xmax_2, ymax_2, label_2] .... ],  
&emsp;img_name_2 : [ [xmin_1, ymin_1, xmax_1, ymax_1, label_1], [xmin_2, ymin_2, xmax_2, ymax_2, label_2] .... ],
  ....  
}

case:
{  
&emsp;'00001.jpg' : [ [  21, &ensp;48, 199, 218, 'cat'], [ 121, &ensp;21, 234, &ensp;78, 'dog'] .... ],  
&emsp;'00002.jpg' : [ [ &ensp;9, 287,  78, 312, 'dog'], [ &ensp;32, &ensp;76, &ensp;90, 112, 'cat'] .... ],
  ....  
}

Transfrom VOC Format

00001.jpg -> 00001.xml
