# Diebold-Mariano-test
This is the library for Diebold-Mariano test implemented with Python.
The libraries Numpy and Scipy are required to use this library.
The inputs should be two lists or arraies. They must be 1 dimension and their lengths should match.
The output is the confidence that the two models which generate these two inputs have obvious performance discrepancy.
If you want to use this library, you should first import the function in it. You can use the following code.
```
from DM_test import DM_test
```
Then, Assuming the two error lists generated by the two models are a and b, you can use the following code to get the confidence that the performance difference between these two models is big.
```
confidence=DM_test(a,b)
```
