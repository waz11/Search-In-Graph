# Part I : converting of code to graph
input: path to code folder\
output: graph in json file\
the graph is a json file, contains two arrays: vertices and edges.\
## vertex
	name - project's name / class's name / method's name
	key - identify key
	type - project / class / method
	attributes - fields in class / arguments in method
## edge
	type - class / method / implements / extends / contains(=argument)
	from - source vertex
	to - destination vertex
### graph as image:
![(Unsaved File)](https://user-images.githubusercontent.com/62445178/147954326-a32f7106-72d2-466e-a859-b1c6d663f3b7.png)

## Instruction:
1. build json file (into: Files/json graphs) contains graph from java project:\
path: Preprocess/graph_builder.py\
function: code_to_graph_in_json_file(project_path, project_name='')\
output: new json file in: Files/json graphs

2. graphviewer - (optional):\
path: Preprocess/create_json_file_for_viewer.py\
function: create_json_file_for_viewer(json_file)\
with BGU vpn, go to: http://khmap.ise.bgu.ac.il/map and import the output file

3. searcher\
path: Searcher/searcher.py\
function:\
load graph to searcher:\
graph = Graph()\
graph.loading_graph_From_json_file(path)\
query = Query(query_text)\
searcher(graph,query)




# Part II : search in graph

## query

query: class list implements class iterable,class list contains class node\
graph:\
![query1](https://user-images.githubusercontent.com/62445178/148056668-61379d48-9b40-4419-ae4a-f3c919d67483.png)


## parser

## graph object

## searcher

## ranker

