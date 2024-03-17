### Creating variable

age = 34
as_as_str = str(age)
print(f"you are {age}")


### Format ###
name = "noam"
final_greeting = "how are you, {}"
jose_gteeting = final_greeting.format(name)
print(jose_gteeting)

name = "bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)