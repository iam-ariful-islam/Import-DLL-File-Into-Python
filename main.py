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