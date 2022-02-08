# the global variable, keeps track of how tall the stack is.
top = -1

def push(stack, item):
    global top
    top += 1
    if(top<len(stack)):
        stack[top] = item
    else:
        stack.append(item)

def pop(stack):
    global top
    try:
        item = stack[top]
        top -= 1
        return item
    except IndexError:
        print("you tried to pop an empty stack!")
        return None

def isPalindrome(s):
    global top
    top = -1
    myStack = []
    n = len(s)
    middle = n//2

    # pushing half of the string onto the stack
    for i in range(middle):
        push(myStack, s[i])

    j = middle if(n%2 == 0) else middle+1

    while(j<n):
        if(top<0):
            return False
        item = pop(myStack)
        if item != s[j]:
            return False
        j += 1
    return True

if __name__ == '__main__':
    print(isPalindrome("hello"), isPalindrome("madam"))
    # should print False True

