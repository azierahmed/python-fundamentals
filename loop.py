#### Loops ####

# Objectives:
# Understand how to loop through a range of numbers
# Understand how to loop through a list
# Understand how to loop through a dictionary
# Understand how to use a while loop
# Understand break and continue statements within loops

# for x in range(0, 10, 1):
# for x in range(0, 10):	# increment of +1 is implied
# for x in range(10):	# increment of +1 and start at 0 is implied

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2



#For Loops through Lists
print("For Loops through Lists -------------------")
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz



#For Loops through Dictionaries
print("For Loops through Dictionaries -------------------")
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc




#While Loops
print("While Loop -------------------")

for count in range(0,5):
    print("looping - ", count)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

# while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

#Else
print("Else -------------------")

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# output: 3, 2, 1, Final else statement




# Note that this else code section is only executed if the while loop runs normally and its conditional is false (whether we never entered the while loop, or we did but eventually the conditional changed from true to false). If instead our while loop is exited prematurely because of a break or return statement, then the else code section will never be executed.

# Loop Control
# We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

# When you want finer control over your loops, use the following statements to do so.

# Break
# The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.

# The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop.

# When loops are nested, a break will only exit from the innermost loop.

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r
#Notice that when the loop got to the letter "i", we stopped looping.




# Continue
# The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.

# The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i


y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1




