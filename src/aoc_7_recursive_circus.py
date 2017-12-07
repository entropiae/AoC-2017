from src.utils import get_file_path

"""
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a
tower of programs that have gotten themselves into a bit of trouble. A
recursive algorithm has gotten out of hand, and now they're balanced
precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large
disc, and on the disc are balanced several more sub-towers. At the bottom
of these sub-towers, standing on the bottom disc, are other programs,
each holding their own disc, and so on. At the very tops of these sub-
sub-sub-...-towers, many programs stand simply keeping the disc below
them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of
these towers. You ask each program to yell out their name, their weight,
and (if they're holding a disc) the names of the programs immediately
above them balancing on that disc. You write this information down (your
puzzle input). Unfortunately, in their panic, they don't do this in an
orderly fashion; by the time you're done, you're not sure which program
gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

...then you would be able to recreate the structure of the towers that
looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth

In this example, tknk is at the bottom of the tower (the bottom program),
and is holding up ugml, padx, and fwft. Those programs are, in turn,
holding up other programs; in this example, none of those programs are
holding up any other programs, and are all the tops of their own towers.
(The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information
is correct. What is the name of the bottom program?
"""


def parse_input(puzzle_input):
    return [parse_row(row) for row in puzzle_input]


def parse_row(row):
    splitted_row = row.split('->')

    first_fragment = splitted_row[0].split(' ')
    name, weight = first_fragment[0], int(first_fragment[1][1:-1])

    if len(splitted_row) > 1:
        sub_names = [n.strip() for n in splitted_row[1].split(',')]
    else:
        sub_names = []
    return name, weight, sub_names


def find_tree_root(rows):
    nodes = [n for n, w, s in rows]
    child_nodes = [ns for n, w, s in rows for ns in s]
    root_set = set(nodes) - set(child_nodes)
    return root_set.pop()


if __name__ == '__main__':
    input_file = get_file_path('recursive_circus.txt')
    with open(input_file) as f:
        raw_puzzle_input = [line.strip() for line in f.readlines()]

    puzzle_input = parse_input(raw_puzzle_input)
    root_program = find_tree_root(puzzle_input)
    print(f'Result for Part 1: {root_program}')
