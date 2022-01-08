# __**MY FINAL BACHELOR PROJECT**__

## PART I : JAVA PROJECT TO GRAPH OBJECT

### Graph object
input: path to code folder\
output: graph object contains vertices & edges
### Vertex fields:
key : identifier
name : class's name / method's name\
type : class / interface / method\
attributes : fields (in class) / arguments (in method)
### Edge
type : class / method / implements / extends / contains(for arguments)\
from : source vertex\
to : target vertex
### ILLUSTRATION:
![src1 (1)](https://user-images.githubusercontent.com/62445178/148656861-98410dbf-f92d-4e69-9fae-c562716cd0e5.png)

## PART II: SEARCH ENGINGE
### Instruction:
1. clone the project
2. install dependencies
graphviewer - (optional):\
path: Preprocess/create_json_file_for_viewer.py\
function: create_json_file_for_viewer(json_file)\
with BGU vpn, go to: http://khmap.ise.bgu.ac.il/map and import the output file

## query
query as text: class list implements class iterable,class list contains class node\
query as graph:\
![query1](https://user-images.githubusercontent.com/62445178/148056668-61379d48-9b40-4419-ae4a-f3c919d67483.png)


## parser
**So far, the parser deals only with some patterns of syntax in query, as described below:**\
	- **class** <ins>[class_name]</ins> **extends class** <ins>[class_name]</ins>\
	- **class** <ins>[class_name]</ins> **implements** <ins>[class_name]</ins>\
	- **class** <ins>[class_name]</ins> **contains class** <ins>[class_name]</ins>\
	- **class** <ins>[class_name]</ins> **contains method** <ins>[method_name]</ins>\
	- **class** <ins>[class_name]</ins> **contains field** <ins>[field_name]</ins>\
	- **method** <ins>method_name</ins> **contains field** <ins>[field_name]</ins>
## searcher

## ranker
semantic similarity - with semach library, for more details go to: https://gsi-upm.github.io/sematch/

