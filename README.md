# CS-350-Permutation-Generation-Algorithms
# Due-Date: March 12th
## TODO:  
###### Add or Pick a task and mark it if your working on it.  
- [X] Implementations, for testing __-Ruben__
- [ ] Pseudocode __-Ruben__
- [ ] Write up of how SJT & Heaps works __-Ruben__
- [X] Implement Test Suite __-Ruben__
- [X] Time Complexity __-Ryan__
- [X] Space Complexity __-Ryan__
- [X] Analyze Termination __-Levi__
- [X] Analyze Correctionness  __-Levi__
- [X] Writing the type of gibberish Litow likes __-Levi__
- [ ] Running code and recording results __-Ryan__
- [ ] Analysis and conclusion's from results __-Group__
##References
-Great verbal walkthrough of both methods: http://www.cs.uni.edu/~wallingf/teaching/cs3530/sessions/session15.html

#### Running The Python code:

>python -i heaps.py  
>heaps([1, 2, 3, 4])

This will start the Python REPL with the heaps file loaded. Make sure to do this in the location where heaps.py is located.

You can also turn on profiling by passing a True parameter after the array:  

>heaps([1, 2, 3, 4], True)
  

##### Running The Test Suite:

The Test Suite runs 20 tests. 
10 for Heaps and 10 for SJT. 
Each test run is completely randomized.
For each test a random set is passed in that contains between 0-6 intergers. (Both positive and negative.)
This set is then ran on Heaps or SJT and the output is compared to the python standard library permutations function.

Because I am using a 3rd party python library that generates random datasets it is important to install these python libraries in a virtual environment in order to not pollute your system python install.

Initlize a virtual environment in current directory:
>virtualenv .

Activate virtual environment:
>source bin/activate

Install virtual environment dependences:
>pip install -r requirements.txt

Deactivate virtual environment:
>deactivate

Run the tests:  
(Make sure this is ran within the virtual environment)
>py.test -v tests.py 

