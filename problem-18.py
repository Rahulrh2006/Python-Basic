# python program to demonstarate identitiy opertor using list
list_a = [10, 20, 30]  
list_b = [10, 20, 30]  
list_c = list_a          

print(f"list_a: {list_a}")
print(f"list_b: {list_b}")
print(f"list_c: {list_c}\n")


print("Using 'is' operator:")

print(f"list_a is list_c: {list_a is list_c}") 

print(f"list_a is list_b: {list_a is list_b}") 

print("-" * 20)

print("Using 'is not' operator:")
print(f"list_a is not list_c: {list_a is not list_c}") 

print(f"list_a is not list_b: {list_a is not list_b}") 

print("-" * 20)

print("Using '==' operator for value comparison:")
print(f"list_a == list_b: {list_a == list_b}") 
print(f"list_a == list_c: {list_a == list_c}") 
