import dis

class Globals:
    def __init__(self):
        self.name = "Global"

class PyByteVM:
    def __init__(self, module, globals_object):
        self.constants = module.co_consts
        self.names = module.co_names
        self.program = module.co_code
        self.nlocals = module.co_nlocals
        self.ip = 0
        self.varnames = module.co_varnames
        self.argcount = module.co_argcount
        self.stack = []
        self.globals = globals_object

    # Pushes co_consts[consti] onto the stack.
    def invoke_LOAD_CONST(self, val):
        self.stack.append(self.constants[val])

    def invoke_LOAD_GLOBAL(self, val):
        self.stack.append(getattr(self.globals, self.names[val]))


    # Implements name = TOS. namei is the index of name in the attribute co_names of the code object.
    # TODO The compiler tries to use STORE_FAST or STORE_GLOBAL if possible.
    def invoke_STORE_NAME(self, val):
        tos = self.stack.pop()
        var_name = self.names[val]
        setattr(self, var_name, tos)
        # store in globals too
        setattr(self.globals, var_name, tos)

    # Pushes the value associated with co_names[namei] onto the stack.
    def invoke_LOAD_NAME(self, val):
        var_name = self.names[val]
        self.stack.append(getattr(self, var_name))

    # Implements TOS = TOS1 + TOS.
    def invoke_BINARY_ADD(self):
        tos = self.stack.pop()
        tos1 = self.stack.pop()
        self.stack.append(tos + tos1)

     # Implements TOS = TOS1 - TOS.
    def invoke_BINARY_SUBTRACT(self):
        tos = self.stack.pop()
        tos1 = self.stack.pop()
        self.stack.append(tos1 - tos)

    def print_bytecode(self, code, name):
        print("-"* 60)
        print(" "*11 + name)
        print("-"*60)
        dis.dis(code)
        print("-"*60)

    # Removes the top-of-stack (TOS) item
    def invoke_POP_TOP(self):
        self.stack.pop()

    # Calls a function
    def invoke_CALL_FUNCTION(self, val):
        # The low byte of argc indicates the number of positional parameters
        num_posn_args = 15 & val
        # the high byte the number of keyword parameters
        num_keyw_args = val >> 8
        posn_args = []
        keyw_args = {}
        # On the stack, the opcode finds the keyword parameters first.
        # For each keyword argument, the value is on top of the key
        for i in range(num_keyw_args):
            value = self.stack.pop()
            key = self.stack.pop()
            keyw_args[key] = value

        # Below the keyword parameters, the positional parameters are on
        # the stack, with the right-most parameter on top
        for i in range(num_posn_args):
            posn_args.append(self.stack.pop())
        posn_args.reverse()
        # Below the parameters, the function object to call is on the stack
        func_code = self.stack.pop()

        # set the keyword pairs
        for key in keyw_args:
            setattr(func_code, key, keyw_args[key])
        # set the positional args
        for i, item in enumerate(posn_args):
            setattr(func_code,func_code.varnames[i], item)
        # pushes the return value
        self.stack.append(func_code.execute())

    # Returns with TOS to the caller of the function.
    def invoke_RETURN_VALUE(self):
        return self.stack.pop()

    # Pushes a new function object on the stack. TOS is the code associated with the function.
    # The function object is defined to have argc default parameters, which are found below TOS.
    def invoke_MAKE_FUNCTION(self, val):
        func_name = self.stack.pop()
        func_code = self.stack.pop()
        def_params = []
        # fetch the default params
        while val > 0:
            def_params.append(self.stack.pop())
            val -= 1
        self.print_bytecode(func_code, func_name)

        def_params.reverse()
        func_vm = PyByteVM(func_code, self.globals)
        # set the default params inside the function object
        for i, item in enumerate(def_params):
            setattr(func_vm,func_vm.varnames[func_vm.argcount-1-i], item)
        self.stack.append(func_vm)


    def invoke_LOAD_FAST(self, val):
        self.stack.append(getattr(self, self.varnames[val]))

    def invoke_STORE_FAST(self, val):
        setattr(self, self.varnames[val], self.stack.pop())


    def execute(self):
        while True:
            op_code = self.program[self.ip]
            self.ip += 1
            if op_code >= dis.HAVE_ARGUMENT:
                low = self.program[self.ip]
                high = self.program[self.ip + 1]
                op_arg = (high << 8) | low
                self.ip += 2
                getattr(self, 'invoke_'+dis.opname[op_code])(op_arg)
            elif op_code == 83: # RETURN_VALUE
                return self.stack.pop()
            else:
                getattr(self, 'invoke_'+dis.opname[op_code])()
            if self.ip >= len(self.program):
                break

if __name__ == '__main__':
    input_file_name = "test_file.py"
    source = ""
    with open(input_file_name, 'r') as f:
       for line in f:
           source += line
    t = compile(source, input_file_name, 'exec')
    globals_object = Globals()
    pyByte = PyByteVM(t, globals_object)
    pyByte.print_bytecode(t, "Main")
    pyByte.execute()
