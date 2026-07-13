branch1 = list(map(int, input("enter the salaries of the branch : ").split()))
branch2 = list(map(int, input("enter the salaries of the branch : ").split()))
salries = branch1 + branch2

salries.sort()
print("combined salaries in the ascending order:  ")
print(salries)