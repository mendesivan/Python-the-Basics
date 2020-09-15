import json

# JSON example

x = '{"name":"Ivan", "age":"30","city":"Boston"}'

# Parse x:
y = json.loads(x)

# The result is a python dictionary
print(y)

# convert into JSON

y = json.dumps(x)
print("---\n",y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Format the json.dump output.

print("---\n",json.dumps(x, indent=2, separators=(", "," = "), sort_keys = False))