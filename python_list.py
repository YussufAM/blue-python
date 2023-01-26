# Make empty list
teams = []
print(teams)

# Adding to the list using the "append" method
teams.append('Toronto')
teams.append('Memphis')
teams.append('Boston')
teams.append('LA')
print(teams)

# adding multiple items to the list using the "extend" method
teams.extend(['Atlanta', 'Miami', 'New York', 'Brooklyn', 'Minnesota', 'Denver'])
print(teams)

# finding the length of the list
print(f'there are {len(teams)} items in the list')

# Using "del" keyword to remove items from the list
del teams[5]
print(teams)
print(f'there are {len(teams)} items in the list')

# using the "remove" method to delete items from the list
teams.remove('Minnesota')
print(teams)
print(f'there are {len(teams)} items in the list')


