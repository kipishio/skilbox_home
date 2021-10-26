import os

def search():






name_file = 'task'
path = os.path.abspath(os.path.join(name_file))
print(path)
path = os.path.abspath(os.path.join('..', '..', '..', '..', 'skilbox'))
print(path)