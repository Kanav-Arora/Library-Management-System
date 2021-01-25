numupper =0
username= input()
for c in username:
    if c.isupper():
        numupper = numupper + 1

if numupper <= 0:
    reason=('username must contain at least one uppercase character')
    print(reason)

numlower =0
for c in username:
    if c.islower():
        numlower = numlower + 1

if numlower <= 0:
    reason=('username must contain at least one lowercase character')
    print(reason)

    if len(username)<8:
        reason = ('username must be greater than 8 characters')
        print(reason)

numdigit=0
for c in username:
    if c.isdigit():
        numdigit = numdigit + 1

if numdigit <= 0:
    reason= ('username must contain at least one number')
    print(reason)

else:
    print(username+" is a valid Username")