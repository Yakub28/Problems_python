# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    new_list=[]
    val=0
    for i in data:
        if i=="i":
            val+=1
        elif i=="d":
            val-=1
        elif i=="s":
            val=val**2
        elif i=="o":
            new_list.append(val)
    return new_list