from src.utils import get_file_path


def steps_to_reach_exit(instructions, next_step):
    steps = 0
    offset = 0
    while 0 <= offset < len(instructions):
        offset, instructions = next_step(offset, instructions)
        steps += 1
    return steps, instructions


def compute_next_step_part_1(offset, instructions):
    current_instruction = instructions[offset]
    next_instruction = offset + current_instruction

    instructions[offset] += 1
    return next_instruction, instructions


def compute_next_step_part_2(offset, instructions):
    """
    Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1.
    Otherwise, increase it by 1 as before.

    Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

    How many steps does it now take to reach the exit?
    """
    current_instruction = instructions[offset]
    next_instruction = offset + current_instruction

    instructions[offset] += -1 if current_instruction > 2 else 1
    return next_instruction, instructions


if __name__ == '__main__':
    input_file_path = get_file_path('twisty_trampolines.txt')

    with open(input_file_path) as f:
        instrs = [int(line.strip()) for line in f.readlines()]

    n_steps, _ = steps_to_reach_exit(instrs, next_step=compute_next_step_part_1)
    print(f'Result for Part 1: {n_steps}')

    n_steps, _ = steps_to_reach_exit(instrs, next_step=compute_next_step_part_2)
    print(f'Result for Part 2: {n_steps}')
