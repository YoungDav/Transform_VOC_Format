# Transform_VOC_Format

ANNOTATION FORMAT:
{ 
  img_name_1 : [ [xmin_1, ymin_1, xmax_1, ymax_1, label_1], [xmin_2, ymin_2, xmax_2, ymax_2, label_2] .... ], 
  img_name_2 : [ [xmin_1, ymin_1, xmax_1, ymax_1, label_1], [xmin_2, ymin_2, xmax_2, ymax_2, label_2] .... ],
  ....
}

case:
{ 
  '00001.jpg' : [ [  21,  48, 199, 218, 'cat'], [121,  21, 234,  78, 'dog'] .... ], 
  '00002.jpg' : [ [   9, 287,  78, 312, 'dog'], [ 32,  76,  90, 112, 'cat'] .... ],
  ....
}

Transfrom VOC Format

00001.jpg -> 00001.xml

<?xml version="1.0" ?>
<annotation>
	<folder>VOC2018</folder>
	<filename>00001.jpg</filename>
	<size>
		<width>1920</width>
		<height>1080</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>cat</name>
		<pose>Frontal</pose>
		<truncated>1</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>21</xmin>
			<ymin>48</ymin>
			<xmax>199</xmax>
			<ymax>218</ymax>
		</bndbox>
	</object>
  	<object>
		<name>dog</name>
		<pose>Frontal</pose>
		<truncated>1</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>121</xmin>
			<ymin>21</ymin>
			<xmax>234</xmax>
			<ymax>78</ymax>
		</bndbox>
	</object>
'</annotation>'
