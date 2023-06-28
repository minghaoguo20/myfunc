from setuptools import setup, find_packages
import os, shutil

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CUR_PATH, 'build')
if os.path.isdir(path):
    print('INFO del dir ', path) 
    shutil.rmtree(path)

# setuptools.setup(
#     name="myfunc",
#     version="0.1.3",
#     author="Minghao GUO",
#     author_email="zjugmh@zju.edu.cn",
#     description="some functions I use frequently",
#     py_modules=['myfunc'],
# )

setup(
    name="myfunc",
    version="0.1.4",
    author="Minghao GUO",
    author_email="ihenrykwok@outlook.com",
    description="some functions I use frequently",
    packages=['myfunc'],
    install_requires=[],
)