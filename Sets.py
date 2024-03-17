nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

# Add the name to the empty set

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.

add_friend = input("what are friends name ?")

user_friends.add(add_friend)

#print(user_friends)
union_list = nearby_people.intersection(user_friends)

print(union_list)
