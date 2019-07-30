from preproc import read_input
from preproc import skills_to_nr
from logic import group

employees = read_input("input.txt")

data = []

for empl in employees.keys():
    data.append([empl,skills_to_nr(employees[empl]),employees[empl]])
    employees[empl] = [skills_to_nr(employees[empl]),employees[empl]]
    #to each emplyee i associate its hash number for the skill list
    #i converted it into a list

print(employees)

target = ['a','b','d','e','i','l','n','o','r','s','t']
#target = ['l','q','s']
target_hash = skills_to_nr(target)

for i in group(data,0,target_hash,0,[]):
    print(i)

