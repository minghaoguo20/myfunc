# get all function names from given python file
def get_func_names(file):
    """
    file: python file
    """
    with open(file, 'r') as f:
        lines = f.readlines()
    func_names = []
    for line in lines:
        if line.startswith("def "):
            func_names.append(line.split()[1].split("(")[0])
    return func_names
