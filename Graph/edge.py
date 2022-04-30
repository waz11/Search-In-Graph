import enum

class EdgeTypeEnum(enum.Enum):
   IMPLEMENTS = "implements"
   EXTENDS = "extends"
   CONTAINS = "contains"
   METHOD = "method"


class Edge():

    def __init__(self, source:int, to:int, type:EdgeTypeEnum):
        self.type :EdgeTypeEnum = type
        self.source :int = source
        self.to :int = to

    def __str__(self):
        return "({}-{}->{})".format(self.source,self.type.value, self.to)
