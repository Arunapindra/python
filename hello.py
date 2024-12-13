# print("hello world")
# -----------
# res = 10 + 20
# print(res)

# --------------
# a = 10 
# b = 20
# res = a + b 
# print(res)
# print("id:" , id(res))
# print("type:", type(res))
#----------------------
"""
this is a block comment
"""
# -----------------------
# sample_str = "this is string"
# print(dir(sample_str))

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

#-----------------------------
txt = "Hello, And Welcome to my world"
print(txt.capitalize())
print(txt.split())
print(txt.index('o'))
print(txt.index('H'))

#-------------------------------

# a = True
# b = False

# print(a and b) # False
# print(a or b)  # True
#-----------------------------------
# a = 2
# b = 4

# print(a + b) # addition
# print(a - b) # substraction
# print(a * b) # multiplication
# print(a / b) # division
# print(b % a) # modulo division: returns remainder
# print(a // b) # Integer division
# print(a ** b) # exponentiation

# 1234 = 10

sample_str = "this is a string"
sample_str[0] = 'T'
# TypeError: 'str' object does not support item assignment

print(sample_str)