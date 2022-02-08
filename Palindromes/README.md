###Problem: Is the given string a palindrome? 
####This is a practice problem relating to stacks, find 2 hours to work on this. If it gets too hard, then use some of my code. Most importantly, you should have an answer to point 1. and understand how my code works.

A palindrome is a string that reads the same from left to right as right to left.
For example: 'madam' and 'rotator' are palindromes, but 'madame' is not a palindrome.

Your task is to design a program that tells whether a string is 
a palindrome or not. If at any point you feel stuck, you can consult the code I wrote in palindromes.py

Here are the steps needed to solve this problem, using a stack:
####1. Think about how you would use a stack to solve this problem.
This step is essential, as you may expect something like this on the A level. Write down the answer
in your own words on paper.
####2. Define push and pop stack methods. 
The contents of the stack can be represented as list. The first item in the list is on the bottom of the stack. 
The last item in the list is at the top of the stack.

So the *push* method
adds an item to the end of a list. For example:
```commandline
stack = []
push(stack, 5)
print(stack[0])
//should print 5
```

For this you will probably find it useful to check out the append() method:
https://www.w3schools.com/python/ref_list_append.asp

The *pop* method, on the other hand, removes and returns the last item
from the list. Removing items from lists is more tricky. But this
problem can be solved without *actually* removing items from the list. We just need to 
define in our own way where the lists *ends* for us. *Hint:
keep track of how tall the stack is.*

So you should have a "global" variable that tracks how tall
the stack is. Read about the concept of global variables here:
https://www.w3schools.com/python/python_variables_global.asp
```commandline
# top is a global variable initialised earlier in the code
stack = [1,2,3,4]
item = pop(stack)
print(item, stack[top])
# should print 4 3
```

####3. Define the isPalindrome function.
Use the concept you have figured out in 1. and the stack methods you've implemented in 2.
First assume that input string is of even length, then try and make it work also for
odd-length strings.
Try doing it on your own. If it gets too difficult, or after you are done, take a look
at the solution on this website:
https://www.geeksforgeeks.org/check-whether-the-given-string-is-palindrome-using-stack/

```commandline
print(isPalindrome("madam"))
# should print out True
print(isPalindrome("hello"))
# should print out False
```

Make sure to set the global "top" variable back to its default
value each time you call isPalindrome.