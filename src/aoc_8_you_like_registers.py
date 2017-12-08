import operator
from functools import reduce

from src.utils import get_file_path

"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent 
assistance with jump instructions, it would like you to compute the 
result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, 
whether to increase or decrease that register's value, the amount by 
which to increase or decrease it, and a condition. If the condition 
fails, skip the instruction without modifying the register. The registers 
all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

 - Because a starts at 0, it is not greater than 1, and so b is not 
   modified.
 - a is increased by 1 (to 1) because b is less than 5 (it is 0).
 - c is decreased by -10 (to 10) because a is now greater than or equal 
   to 1 (it is 1).
 - c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). 
However, the CPU doesn't have the bandwidth to tell you what all the 
registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the 
instructions in your puzzle input?

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any 
register during this process so that it can decide how much memory to 
allocate to these operations. For example, in the above instructions, the 
highest value ever held was 10 (in register c after the third instruction 
was evaluated).
"""

# Map each operator found in input to the corresponding function
ops_mapping = {
    'inc': operator.add,
    'dec': operator.sub,
    '==': operator.eq,
    '!=': operator.ne,
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le
}


def get_max_values(instructions):
    registers_history = process_instructions(instructions)

    max_value_in_output = max(registers_history[-1].values())
    max_absolute_value = max(value for register in registers_history for value in register.values())

    return max_value_in_output, max_absolute_value


def eval_row(row):
    """ Convert each row in executable instructions """
    (target_register, op, value), (compared_register, compare_op, compared_value) = row
    return build_apply(target_register, op, value), build_apply_if(compared_register, compare_op, compared_value)


def build_apply(target_register, op, value):
    def _apply(registers):
        register_output_value = ops_mapping[op](registers.get(target_register, 0), value)
        updated_registers = {**registers, **{target_register: register_output_value}}
        return updated_registers

    return _apply


def build_apply_if(target_register, op, value):
    def _apply_if(registers):
        return ops_mapping[op](registers.get(target_register, 0), value)

    return _apply_if


def process_instructions(instructions):
    return reduce(process_instruction, instructions, [dict()])


def process_instruction(acc, instruction):
    registers = acc[-1]
    apply, apply_if = instruction
    updated_registers = apply(registers) if apply_if(registers) else registers
    acc.append(updated_registers)
    return acc


def parse_input(unparsed_input):
    return [parse_row(row) for row in unparsed_input]


def parse_row(row):
    target_register, op, value, _, compared_register, compare_op, compared_value = row.split(' ')
    return (target_register, op, int(value)), (compared_register, compare_op, int(compared_value))


if __name__ == '__main__':
    file_path = get_file_path('registers.txt')

    with open(file_path) as f:
        raw_puzzle_input = [line.strip() for line in f.readlines()]

    instructions = [eval_row(row) for row in parse_input(raw_puzzle_input)]
    max_value, absolute_max = get_max_values(instructions)

    print(f'Result for Part 1: {max_value}')
    print(f'Result for Part 2: {absolute_max}')
