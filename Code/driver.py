from its import Its
from student import Student
import copy

it = Its()
stu = Student()
stu.states = copy.deepcopy(it.states)
stu.play(it)


