import string
import random

password = ''.join(random.choices(string.ascii_lowercase, k=12))
print("Generated password: " + password)
