# Part I : converting of code to graph

input: path to code folder

output: graph in json file

the graph is a json file, contains two arrays: vertices and edges.

## vertex
	name - project's name / class's name / method's name
	key - identify key
	type - project / class / method
	attributes - fields in class / arguments in method
## edge
	type - class / method / implements / extends
	from - source vertex
	to - destination vertex

### graph as image:
![(Unsaved File)](https://user-images.githubusercontent.com/62445178/147954326-a32f7106-72d2-466e-a859-b1c6d663f3b7.png)

##steps:
1. build json file (into: Files/json graphs) contains graph from java project:

folder: Preprocess

file: graph_builder

function: code_to_graph(project_path,project_name, output_path)

2. optional: graph viewer

with BGU vpn, go to: http://khmap.ise.bgu.ac.il/map

and import the output file from the folder: Files/json graphs for viewer



# Part II : search in graph

## query

## parser

## graph object

## searcher

## ranker

