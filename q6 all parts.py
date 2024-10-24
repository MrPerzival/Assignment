# Problem-6: Marks Management
marks = {
    'Subu': {'Maths': 88, 'Eng': 60, 'SSt': 95},
    'Amol': {'Maths': 78, 'Eng': 68, 'SSt': 89},
    'Raka': {'Maths': 56, 'Eng': 66, 'SSt': 77}
}

# a) Print Amol's marks in English
print(marks['Amol']['Eng'])

# b) Set Raka's marks in Maths to 77
marks['Raka']['Maths'] = 77

# c) Sort dictionary by name
sorted_marks = dict(sorted(marks.items()))
print(sorted_marks)
