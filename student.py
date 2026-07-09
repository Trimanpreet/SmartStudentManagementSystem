class Student:

    def __init__(self, roll, name, age, course, marks):

        self.roll = roll
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }
