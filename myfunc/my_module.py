import os, json

# ##########################################

def my_add(a, b):
    print(f"{a} + {b} = {a+b}")
    return a + b

def greet():
    print("Hello, World!")

# ##########################################

repo = "/home/test/tool/myfunc/file/var/"

# function: given a variable, save it to a json file in repo
def var_save(var, name):
    """
    var: variable to be saved
    name: name of the variable
    """
    name = name[-5:] if ".json" == name[-5:] else name
    name = os.path.join(repo, name + ".json")
    with open(name, 'w') as f:
        json.dump(var, f)
    return name

# function: given a variable name, load it from a json file in repo
def var_load(name):
    """
    name: name of the variable
    """
    name = name[-5:] if ".json" == name[-5:] else name
    name = repo + name + ".json"
    with open(name, 'r') as f:
        var = json.load(f)
    return var
