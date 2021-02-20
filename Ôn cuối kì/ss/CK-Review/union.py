from abc import *
import enum
from dataclasses import dataclass
class Shape(enum.Enum):
    Circle=0
    Triangle=1
    Rectangle=2

class Color(enum.Enum):
    Red=0
    Green=1
    Blue=2
@dataclass
class Figure(ABC):
    Form: Shape
    Filled: bool
    Colors: Color

@dataclass
class Circle(Figure):
    Diameter: float

@dataclass
class Triangle(Figure):
    Leftside:int
    Rightside: int
    Angle: float

@dataclass
class Rectangle(Figure):
    Side1:int
    Side2: int

circle1 = Circle(Shape(0),True,Color(0),3.0)
triangle = Triangle(Shape(1),True,Color(1),3,4,5)

print(circle1.Diameter)
