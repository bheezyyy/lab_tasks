import os
import json

# Ensure folders exist
os.makedirs("data/samples", exist_ok=True)
os.makedirs("data/out", exist_ok=True)

# 1. Create a dummy JSON file
people = [
    {"name": "Emeka Okonkwo", "role": "Engineer", "age": "30", "country": "Nigeria"},
    {"name": "Joao Baptista", "role": "Designer", "age": "25", "country": "Angola"},
    {"name": "Nneka Adebayo", "role": "Manager", "age": "40", "country": "Nigeria"},
    {"name": "Ana Mateus", "role": "Data Analyst", "age": "28", "country": "Angola"},
    {"name": "Chinedu Eze", "role": "Developer", "age": "32", "country": "Nigeria"}
]
with open("data/samples/people.json", "w") as f:
    json.dump(people, f, indent=2)

# 2. Create a dummy Text file
text = """Python is powerful.
Python is simple.
Data science needs Python.
CLI tools are useful.
Python Python Python."""
with open("data/samples/text.txt", "w") as f:
    f.write(text)

print("Setup complete: Test files created in 'data/samples/'")