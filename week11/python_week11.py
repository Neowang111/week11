print("It worked!")
# Name: Neo Wang

x = None

print("Level 3 running!")

x = 3            
y = 3.0        
name = "Max"    
is_happy = True 
z = None       
items = ["apple", 5, False]  

print("Level 4 running!")

"""
Variables can be ANYTHING, because it's just a name, as long as they follow these rules.

 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_)
 2. The rest of the variable name can contain letters, numbers, or underscores
 3. Variable names are case-sensitive (myVar ≠ myvar)
 4. Variable names cannot be Python keywords (like `class`, `if`, `while`, etc.)
5. Variable names cannot start with a number

 Examples of **invalid** variable names:
3dogs = "bad"          # Starts with a number
my-variable = 5        # Hyphen is not allowed
def = "nope"           # 'def' is a reserved keyword
$$$Variable = "bad"    # Special symbols are not allowed
"""


# Level 6: Using the type() function to understand data types

x = type(3)          
y = type("Hello")   
z = type(True)      

print(x)
print(y)
print(z)

# Level 7: Using print() to check what data types are being stored

a = 5            
b = 3.14         
c = "Hello"      
d = True         
e = None         
f = [1, 2, 3]    

type_a = type(a)
type_b = type(b)
type_c = type(c)
type_d = type(d)
type_e = type(e)
type_f = type(f)


print(type_a)    
print(type_b)   
print(type_c)     
print(type_d)     
print(type_e) 
print(type_f)  
