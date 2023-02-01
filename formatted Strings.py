import datetime
first = 'john'
last = 'lederman'

meassgae = first + '[' + last + ']'+ 'is a coder'
print(meassgae) ## --> this solution is too long

msg = f'{first} [{last}] is a coder'
print(msg)



date = datetime.datetime.now()
print(date)

msg1= f'{date} is the current date you fucker'
print(msg1)