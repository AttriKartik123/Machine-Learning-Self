data = {1: 'Harleen', 2: 'Kartik', 3: 'Imanpal', 4: 'Harsh'}
print(data)

print(data[2])

# print(data[5])  # Would give KeyError

print(data.get(1))
print(data.get(5, "Not found"))

# Creating dictionary using lists
keys = ['navin', 'harsh', 'akash']
values = ['CPP', 'C', 'JS']

data = dict(zip(keys, values))
print(data)

# Adding data to dictionary
data['Monika'] = 'C-Sharp'
print("After adding:", data)

# Deleting data
del data['harsh']
print("After deleting:", data)

# Dictionary inside dictionary and list
prog = {
    'JS': 'Atom',
    'C sharp': 'VS Code',
    'Python': ['PyCharm', 'Sublime'],
    'Java': {'JSE': 'NetBeans', 'JEE': 'Eclipse'}
}

print(prog)
print(prog['JS'])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JEE'])   # ✅ Correct output
