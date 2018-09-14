# Lab 4 Employee Class Define and Use Case


class Employee:
    emp_count = 0  # Class Attribute Data Member
    emp_avg = 0

    def __init__(self, nam, fam, sal, dep):
        self.name = nam
        self.family = fam
        self.salary = sal
        self.department = dep                # Data Attribute
        Employee.emp_count += 1
        Employee.emp_avg += sal

    def getempcount(self):
        return self.__class__.emp_count

    def getname(self):
        return self.name

    def getsalary(self):
        return self.salary

    def getfamily(self):
        return self.family

    def getdep(self):
        return self.department

    def avg_sal(self):
        average_sal = self.__class__.emp_avg / self.__class__.emp_count
        return average_sal


# Inherting the base class Employee


class FullEmployee(Employee):

    def __init__(self, nam, fam, sal, dep, bon):
        Employee.__init__(self, nam, fam, sal, dep)  # Call base class constructor
        self.bonus = bon

    def getbonus(self):
        return self.bonus


if __name__ == "__main__":
    emp1 = Employee('Razu', 'B', 30000, 'IT')
    emp2 = Employee('Swati', 'A', 30000, 'HR')
    boss = FullEmployee('Adam', 'M', 30000, 'CEO', 50000)

    print('Employee Name : ', emp1.getname(), 'Employee Salary : ', emp1.getsalary(), 'Average Salary : ',
          emp1.avg_sal(), 'Employee Family : ', emp1.family, 'Employee Family :', emp1.getempcount())
    
    print('Employee Name : ', boss.getname(), 'Employee Salary : ', boss.getsalary(), 'Average Salary : ',
          boss.avg_sal(), 'Employee Family : ', boss.family, 'Employee Family :', emp1.getempcount())











