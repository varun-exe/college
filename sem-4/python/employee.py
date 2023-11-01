class employee:
    def __init__(self,name,id,dept,salary):
        self.name=name
        self.id=id
        self.dept=dept
        self.salary=salary

    def update(self,dept,income):
        if self.dept==dept:
            self.salary+=income

emp=[]
n=int(input("enter number of employees: "))
for i in range(n):
    name=input(f"name of employee{i + 1}")
    id=int(input(f"id of employee{i + 1}"))
    dept = input(f"dept of employee{i + 1}")
    salary = float(input(f"salary of employee{i + 1}"))
    emp.append(employee(name, id, dept, salary))

for i in emp:
    print(f"name:{i.name} id:{i.id} dept:{i.dept} salary:{i.salary}")

income=int(input("enter salary hike: "))
dept=input("enter dept: ")
for i in emp:
    {i.update(dept,income)}
for i in emp:
    print(f"name:{i.name} id:{i.id} dept:{i.dept} salary:{i.salary}")
