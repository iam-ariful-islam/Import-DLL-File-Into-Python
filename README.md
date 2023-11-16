# Import DLL File Into Python
Importing a custom dll built with C# into a python project and access the functions inside the dll with the help of [pythonnet](https://pypi.org/project/pythonnet/) or open command prompt and type for installation

```python
# install pythonnet
pip install pythonnet
```

### Project Structure
* DLL file contains the C# solution
* The python solution using C# dll file

### Dll File Code
```C#
namespace CalcProject
{
    public class calculate
    {
        /// accept two integer parameters a and b
        /// return sum of two numbers
        /// Add(3, 2) and return 5
        public int Add(int a, int b)
        {
            return a + b;
        }
    }
}
```

## Installation
First [download](https://www.python.org/downloads/), install and configure [python](https://www.python.org/doc/). Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install on.
* For create dll file of C#, first write C# code then run, after successfully run goto build folder of project file for collect dll file.

## Task Requirments & Testing Environment
this project is developed using all new os, software and tools.

* **Operating System :** Windows10
* **Software :** Python3.11 and Visual Studio Code


### Python Code
```python
import clr


# add reference to the library/dll
clr.AddReference("dlls/CalcProject")


# from namespace name import class name
from CalcProject import calculate


# create object of the class
cls_obj = calculate()


# call the function with class object
# the function from dll that you want to access
result = cls_obj.Add(3, 4)

# output from dll file
print('Output from dll file:', result)   # 7
# normal python output
print(f'Output from python: {3 + 4 = }') # 3 + 4 = 7
```

## Notes
The `requirements.txt` file, lists of all the python libraries that my "**_Import DLL File Into Python_**" depends on and installs those packages from the file:

```
pip install -r requirements.txt
```

### **or**

```
sudo pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## For more or connect with me

<p align='center'>
  <a href="https://github.com/iam-ariful-islam"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/am_ariful_islam"><img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/im-ariful-islam"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/jonakisoft.net/"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>

## License

The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)