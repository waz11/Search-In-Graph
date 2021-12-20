# converting source code to graph:

the graph is a json file, contains two arrays: vertices and edges.


## vertex

	name - project name / class name / method name
	key - identify key
	type - project / class / method
	attributes - fields in class / arguments in method


## edge

	type - class / method / implements / extends
	from - source vertex
	to - destination vertex
