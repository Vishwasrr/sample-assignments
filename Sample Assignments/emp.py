class Employee:

    DEPARTMENT = 'SARD'
    PROJECT = 'Automation'

    def __init__(self, name, salary, desgn):

        self.name = name
        self.salary = salary
        self.desgn = desgn
        self.current_base = 0

    @staticmethod
    def timings():
        print('Login timings: 9:00am')
        print('Logout timings: 6:00am')

    @property
    def designation(self):
        return self.DEPARTMENT

    @designation.setter
    def designation(self, desgn):
        self.desgn = desgn

    @designation.deleter
    def designation(self):
        del self.designation

    @classmethod
    def set_project(cls, new_project):
        cls.PROJECT = new_project
        # return cls.PROJECT


jess = Employee('Jessica', 1000, 'employee')
# del jess
rob = Employee('Robert', 10000, 'boss')
print('name:', jess.name)
print('salary:', jess.salary)
print(jess.desgn)
del jess.desgn
print(jess.desgn)
jess.desgn = "DRAS"
print(jess.desgn)
print(jess.PROJECT)
jess.set_project('Manual')
Employee.timings()
jess.timings()
print(jess.PROJECT)
print(rob.PROJECT)
print(jess.salary)
