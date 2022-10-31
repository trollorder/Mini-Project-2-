
def merge(array, p, q, r, byfunc):
    nleft = q - p + 1
    nright = r - q
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left = 0
    right = 0
    dest = p
    while (left<nleft) and (right<nright):
        if byfunc(left_array[left]) <= byfunc(right_array[right]):
            array[dest] = left_array[left]
            left+=1
        else:
            array[dest] = right_array[right]
            right+=1
        dest+=1
    while left<nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right<nright:
        array[dest] = right_array[right]
        right+=1
        dest+=1
    return array

def mergesort_recursive(array, p, r, byfunc):
    if (r-p > 0):
        q = (p+r)//2
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)

def mergesort(array, byfunc = lambda x:x):
    p = 0
    n = len(array)
    r = n-1
    mergesort_recursive(array, p, r, byfunc)

class Stack:

    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        n = len(self.__items)
        if n > 0:
            x = self.__items[-1]
            self.__items.pop()
            return x

    def peek(self):
        n = len(self.__items)
        if n == 0:
            return None
        else:
            return self.__items[-1]

    @property
    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return(len(self.__items))


class EvaluateExpression:
  # copy the other definitions
  # from the previous parts
    valid_char = '0123456789+-*/() '
    def __init__(self, string=""):
        self.expr = string
        self.operators = '+-/*()'
        self.operands = '0123456789'

    @property
    def expression(self):
        return self.expr

    @expression.setter
    def expression(self, new_expr):
        for i in new_expr:
            if i not in self.valid_char:
                self.expr = ""
                return
        self.expr = new_expr
        return
    
    def insert_space(self):
        stringgy = ''
        for i in self.expr:
            if i in self.operators:
                stringgy += " " + i + " "
            else:
                stringgy += i 
        return stringgy
    
    def process_operator(self, operand_stack, operator_stack):
#         print(operand_stack.size)
        pp = operator_stack.pop()

        lefty = operand_stack.pop()
    
        righty = operand_stack.pop()

        if pp == "+":
            operand_stack.push(lefty + righty)
        if pp == "-":
            operand_stack.push(righty - lefty)
        if pp == "*":
            operand_stack.push(lefty * righty)
        if pp == "/":
            operand_stack.push(righty // lefty)

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        char = expression.split()
        while len(char) != 0:
            r = char.pop(0)
            if r in self.operands:
                pp = r
                operand_stack.push(int(pp))                    
            elif r == "+" or r== "-":
                while operator_stack.is_empty == False:
                    x = operator_stack.peek()
                    if x == "(" or x == None:
                        break
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(r)

            elif r == "*" or r == "/":
                while operator_stack.is_empty == False:
                    x = operator_stack.peek()
                    if x == "(" or x == "+" or x == "-":
                        break
                    if x in "*/":
                        self.process_operator(operand_stack, operator_stack)
                operator_stack.push(r)
            
            elif r in "()":
                if r =="(":
                    operator_stack.push(r)
                    if char[1] == ")":
                        operator_stack.pop()
                if r ==")":
                    self.process_operator(operand_stack, operator_stack)
                    x = operator_stack.peek()
                    if x == "(":
                        operator_stack.pop()
#             print(operand_stack.peek())
                        
        while operator_stack.size > 0:
            self.process_operator(operand_stack,operator_stack)
        
        return operand_stack.peek()
                    
                
                    
expr3 = EvaluateExpression("((1+3+3) * (2+4+4)) / (2)")
print(expr3.evaluate())
                    

        


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





