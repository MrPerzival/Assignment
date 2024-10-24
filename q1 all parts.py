# Problem-1: Cricket Team Selection
team = ['MS Dhoni', 'Virat Kohli', 'Rohit Sharma', 'Shreyas Iyer', 'Hardik Pandya', 'Ravindra Jadeja', 'Jasprit Bumrah']

# a) Add Suryakumar Yadav right before Jasprit Bumrah
team.insert(team.index('Jasprit Bumrah'), 'Suryakumar Yadav')

# b) Append Mohammed Shami at the end of the list
team.append('Mohammed Shami')

# c) Remove Shreyas Iyer due to injury
team.remove('Shreyas Iyer')

# d) Correct Hardik Pandya to Hardik
team[team.index('Hardik Pandya')] = 'Hardik'

# e) Sort the list alphabetically
team.sort()

# f) Reverse the sorted list
team.reverse()

print(team)
