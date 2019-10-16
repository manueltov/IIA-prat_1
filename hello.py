#isto é um comentario só pra testar e aprender
print ('Hello World!')
print ('Hello World!');  #funciona tambem por o ; a mais

frase = "Hello World"

print(frase)

listinha = [0, 1, 2, 7, 8, 4, 3]

group = ["Bob", 23, "George", 72, "Myriam", 29]


# -----------------------------------------------------------

class Employee():
    def __init__(self, employeeName, taxDeductions=1, maritalStatus="single"):
        self.employeeName = employeeName
        self.taxDeductions = taxDeductions
        self.maritalStatus = maritalStatus

    def __str__(self):
        return "{0},{2},{1}".format(self.employeeName, self.taxDeductions, self.maritalStatus)

x = Employee("João")
y = Employee("Maria",2)
z = Employee("Manuel",maritalStatus="married")
x.taxDeductions = 3

for p in [x,y,z] :
    print(p)
