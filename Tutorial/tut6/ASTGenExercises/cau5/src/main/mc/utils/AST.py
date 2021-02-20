from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List

class AST(ABC):
    pass

class Type(AST):
    pass

@dataclass
class VarDecl(AST):
    typ:Type
    id:str

    def __str__(self):
        return "VarDecl(" +  self.id + "," + str(self.typ) + ")"
    
@dataclass
class Program(AST):
    decls:List[VarDecl]

    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decls) + "])"

@dataclass
class ArrayType(Type):
    eleType:Type
    dim: int

    def __str__(self):
        return "ArrayType(" + str(self.eleType) + "," + str(self.dim) + ")"

class IntType(Type):
    def __str__(self):
        return "IntType"

class FloatType(Type):
    def __str__(self):
        return "FloatType"



