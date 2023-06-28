# myfunc

## tutorial of setuptools

### prompt

How to make my own python package named myfunc using setuptools? Teach me with an example.

### response from gpt3.5

Sure! I can walk you through the process of creating a Python package named "myfunc" using setuptools. Here's a step-by-step example:

Step 1: Project Structure
Create a directory structure for your package. Open your terminal or command prompt and navigate to the directory where you want to create the package. Run the following commands:

```
mkdir myfunc
cd myfunc
```

Step 2: Create Files
Inside the "myfunc" directory, create the necessary files:

```
touch myfunc/__init__.py
touch myfunc/my_module.py
touch setup.py
```

Step 3: Define Package Code
Open the "myfunc/__init__.py" file and add the following code:

```python
from .my_module import my_function
```

Create your desired functionality in the "myfunc/my_module.py" file. For example, let's define a simple function that adds two numbers:

```python
def my_function(a, b):
    return a + b
```

Step 4: Create setup.py
Open the "setup.py" file and add the following code:

```python
from setuptools import setup

setup(
    name='myfunc',
    version='0.1',
    packages=['myfunc'],
)
```

Make sure to replace the package name, version, and packages list according to your project.

Step 5: Build and Install the Package
In your terminal or command prompt, navigate to the "myfunc" directory. Run the following command to build and install the package:

```
python setup.py install
```

Step 6: Test the Package
You can now test your package by importing it in a Python script or interactive session. Create a new Python file (e.g., "main.py") with the following code:

```python
from myfunc import my_function

result = my_function(2, 3)
print(result)
```

Save the file and run it:

```
python main.py
```

If everything is set up correctly, you should see the output `5`, which is the result of calling the `my_function` from your package.

That's it! You've successfully created a Python package named "myfunc" using setuptools. You can now distribute and install your package on other systems by using the same installation process (`python setup.py install`).

