from typing import List

from src.utils import wrap_index, get_file_path

"""
--- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a memory
reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any
number of blocks. The goal of the reallocation routine is to balance the
blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the
memory bank with the most blocks (ties won by the lowest-numbered memory
bank) and redistributes those blocks among the banks. To do this, it
removes all of the blocks from the selected bank, then moves to the next
(by index) memory bank and inserts one of the blocks. It continues doing
this until it runs out of blocks; if it reaches the last memory bank, it
wraps around to the first one.

The debugger would like to know how many redistributions can be done before
a blocks-in-banks configuration is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

 - The banks start with 0, 2, 7, and 0 blocks. The third bank has the
   most blocks, so it is chosen for redistribution.
 - Starting with the next bank (the fourth bank) and then continuing to
   the first bank, the second bank, and so on, the 7 blocks are spread
   out over the memory banks. The fourth, first, and second banks get two
   blocks each, and the third bank gets one back. The final result
   looks like this: 2 4 1 2.
 - Next, the second bank is chosen because it contains the most blocks
   (four). Because there are four memory banks, each gets one block. The
   result is: 3 1 2 3.
 - Now, there is a tie between the first and fourth memory banks, both of
   which have three blocks. The first bank wins the tie, and its three
   blocks are distributed evenly over the other three banks, leaving it
   with none: 0 2 3 4.
 - The fourth bank is chosen, and its four blocks are distributed such
   that each of the four banks receives one: 1 3 4 1.
 - The third bank is chosen, and the same thing happens: 2 4 1 2.

At this point, we've reached a state we've seen before: 2 4 1 2 was already
seen. The infinite loop is detected after the fifth block redistribution
cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many
redistribution cycles must be completed before a configuration is produced
that has been seen before?
"""


def cycles_before_infinite_loops(configuration):
    already_seen_configurations = set()

    while True:
        configuration = reallocate_memory(configuration)

        if tuple(configuration) in already_seen_configurations:
            break

        already_seen_configurations.add(tuple(configuration))

    return len(already_seen_configurations) + 1, configuration


def reallocate_memory(memory_banks: List[int]):
    max_value = max(memory_banks)
    max_value_idx = memory_banks.index(max_value)

    memory_banks[max_value_idx] = 0
    current_bank_idx = max_value_idx + 1

    while max_value > 0:
        current_bank_idx = wrap_index(current_bank_idx, memory_banks)

        memory_banks[current_bank_idx] += 1
        max_value -= 1
        current_bank_idx += 1
    return memory_banks


def parse_input(raw_in):
    return [int(x) for x in raw_in.split('\t')]


if __name__ == '__main__':
    input_file = get_file_path('memory_reallocation.txt')
    with open(input_file) as f:
        raw_puzzle_input = f.readline()

    puzzle_input = parse_input(raw_puzzle_input)
    reallocation_before_loop, final_configuration = cycles_before_infinite_loops(puzzle_input)
    print(f'Result for Part 1: {reallocation_before_loop}')
    reallocation_before_loop, final_configuration = cycles_before_infinite_loops(final_configuration)
    print(f'Result for Part 1: {reallocation_before_loop - 1}')
