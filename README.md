## Dependency
 ```
 pip install -r requirements.txt
 ```

## Part I: JAVA Project To Graph Object
### Graph object
software projectβs code graph πΊ=(π,πΈ) is an unweighted directed graph. Vertex set ππΊ includes all nodes composed of classes, interfaces and methods. For each edge π(π’,π£)βπΈπΊ,βπ’ππ£βπππ, where π’ππ£ means node π’ and node v have a relationship R.\
input: path to code folder\
output: graph object contains vertices & edges
### Vertex Object:
key : identifier
name : class's name / method's name\
type : class / interface / method\
attributes : field / argument
### Edge Object:
type : class / method / implements / extends / contains(argument or field)\
from : source vertex\
to : target vertex
### ILLUSTRATION:
![IterableList](https://user-images.githubusercontent.com/62445178/166119423-c897ad8f-f291-4b67-b251-0ba3ecc67242.png)

# Part II: Search Engine

## Algorithm 1 - Greedy Search approach:
In each iteration the algorithm tries to find the most similar class to the next class of the query using similarity function that considers type similarity, structure similarity and label similarity.
### Instructions
1. download the sematch package from: [link](https://files.pythonhosted.org/packages/f4/1a/09377bdde1fcf4ede770c631e50199511a07921cf11dc66d3a83f2514277/sematch-1.0.4.tar.gz) 
2. add the sematch folder to the following path: algorithm1/Ranker/sematch

### Query
query as text: class list implements class iterable,class list contains class node\
query as graph:\
![query1](https://user-images.githubusercontent.com/62445178/148056668-61379d48-9b40-4419-ae4a-f3c919d67483.png)
#### Query Parser
**So far, the parser deals only with some patterns of syntax in query, as described below:
- class [class_name] extends class [class_name]
- class [class_name] implements class [class_name]
- class [class_name] contains class [class_name]
- class [class_name] contains method [method_name]
- class [class_name] contains field [field_name]
- method method_name contains field [field_name]

### Ranker
semantic similarity - with semach library, for more details go to: https://gsi-upm.github.io/sematch/


## Algorithm 2 - Beam Search approach:
### Instructions
1. download the cc.en.300.bin file from: [link](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz)
2. add the file to the following path: algorithm2/model/cc.en.300.bin

### Query
#### Query Parser
### Ranker

