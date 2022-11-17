#-----------------------------------------------------------------------------------------------------------------------------------------------     
# [1] For Loops
# [2] While Loops
#--------------------------------------------------------------------------------------------------------------



# For Loops ------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 


# Looping Through a String -------------------------
for x in "banana":
  print(x) 


# The break Statement ----------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

# The continue Statement ----------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 

# The range() Function -------------------------------
for x in range(6):
  print(x) 



# while Loop ------------------------------------------
i = 1
while i < 6:
  print(i)
  i += 1

# ------------------------------------------------------------------------------------------------------------------------------------------------
