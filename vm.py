import dis
import operator

COMPARISION = [
    operator.lt,
    operator.le,
    operator.eq,
    operator.ne,
    operator.gt,
    operator.ge
]

class Globals:
    def __init__(self):
        self.name = "Global"

class PyByteVM:
    def __init__(self, module=None, globals_object=None, parent=None):
        if parent is None:
            self.constants = module.co_consts
            self.names = module.co_names
            self.program = module.co_code
            self.nlocals = module.co_nlocals
            self.ip = 0
            self.varnames = module.co_varnames
            self.argcount = module.co_argcount
            self.stack = []
            self.globals = globals_object
            self.parent = None
        else:
            self.constants = parent.constants
            self.names = parent.names
            self.program = parent.program
            self.nlocals = parent.nlocals
            self.ip = parent.ip
            self.varnames = parent.varnames
            self.argcount = parent.argcount
            self.stack = []
            self.globals = parent.globals
            self.parent = parent
        self.context = None
        self.var_contexts = {}

    # Pushes co_consts[consti] onto the stack.
    def invoke_LOAD_CONST(self, val):
        self.stack.append(self.constants[val])

    def invoke_LOAD_GLOBAL(self, val):
        self.stack.append(self.get_from_exec_frame(self.globals, self.names[val]))

    def set_in_exec_frame(self, context, var_name, var_value):
        # self.context contains the context that get_from_exec_frame() found the attribute in
        if var_name not in self.var_contexts:
            setattr(context, var_name, var_value)
        else:
            setattr(self.var_contexts[var_name], var_name, var_value)

    # if attribute can't be found in current context recurse up to it's parent context
    def get_from_exec_frame(self, context, var_name):
        # first set this to None to indicate current context
        self.context = None
        while context is not None:
            try:
                var_value = getattr(context, var_name)
                self.context = context
                break
            except AttributeError:
                context = context.parent
        self.var_contexts[var_name] = context
        if context is None:
            print('huh')
        return var_value

    # Implements name = TOS. namei is the index of name in the attribute co_names of the code object.
    # TODO The compiler tries to use STORE_FAST or STORE_GLOBAL if possible.
    def invoke_STORE_NAME(self, val):
        tos = self.stack.pop()
        var_name = self.names[val]
        self.set_in_exec_frame(self, var_name, tos)
        # store in globals too
        self.set_in_exec_frame(self.globals, var_name, tos)

    # Pushes the value associated with co_names[namei] onto the stack.
    def invoke_LOAD_NAME(self, val):
        var_name = self.names[val]
        self.stack.append(self.get_from_exec_frame(self, var_name))

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
        print(" "*26 + name)
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
            self.set_in_exec_frame(func_code, key, keyw_args[key])
        # set the positional args
        for i, item in enumerate(posn_args):
            self.set_in_exec_frame(func_code,func_code.varnames[i], item)
        # pushes the return value
        self.stack.append(func_code.execute())

    # Returns with TOS to the caller of the function.
    def invoke_RETURN_VALUE(self):
        return self.stack.pop()

    def invoke_POP_JUMP_IF_FALSE(self, val):
        if not self.stack.pop():
            self.ip = val

    def invoke_JUMP_FORWARD(self,val):
        self.ip += val

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

        # def_params.reverse()
        func_vm = PyByteVM(module=func_code, globals_object=self.globals)
        # set the default params inside the function object
        for i, item in enumerate(def_params):
            self.set_in_exec_frame(func_vm,func_vm.varnames[func_vm.argcount-1-i], item)
        self.stack.append(func_vm)

    def invoke_COMPARE_OP(self, val):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(COMPARISION[val](a,b))

    def invoke_LOAD_FAST(self, val):
        self.stack.append(self.get_from_exec_frame(self, self.varnames[val]))

    def invoke_STORE_FAST(self, val):
        self.set_in_exec_frame(self, self.varnames[val], self.stack.pop())

    def invoke_SETUP_LOOP(self, val):
        loop_exec_frame = PyByteVM(parent=self)
        self.ip += val
        loop_exec_frame.execute()

    def invoke_JUMP_ABSOLUTE(self, val):
        self.ip = val

    def invoke_INPLACE_ADD(self):
        # self.stack[-1] = self.stack[-2] + self.stack[-1]
        self.invoke_BINARY_ADD()

    def invoke_INPLACE_SUBTRACT(self):
        # self.stack[-1] = self.stack[-2] - self.stack[-1]
        self.invoke_BINARY_SUBTRACT()

    def execute(self):
        while True:
            op_code = self.program[self.ip]
            print(dis.opname[op_code], op_code)
            self.ip += 1
            if op_code >= dis.HAVE_ARGUMENT:
                low = self.program[self.ip]
                high = self.program[self.ip + 1]
                op_arg = (high << 8) | low
                self.ip += 2
                self.get_from_exec_frame(self, 'invoke_'+dis.opname[op_code])(op_arg)
            elif op_code == 83: # RETURN_VALUE
                return self.stack.pop()
            elif op_code == 87: # POP_BLOCK
                return
            else:
                self.get_from_exec_frame(self, 'invoke_'+dis.opname[op_code])()
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
    pyByte = PyByteVM(module=t, globals_object=globals_object)
    pyByte.print_bytecode(t, "Main")
    pyByte.execute()
