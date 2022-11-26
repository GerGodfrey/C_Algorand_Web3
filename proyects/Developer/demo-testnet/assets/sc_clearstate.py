from pyteal import *

"""Basic Counter Application"""

def clear_state_program():
    program = Return(Int(1))
    return compileTeal(program, Mode.Application, version=6)

# print out the results
print(clear_state_program())