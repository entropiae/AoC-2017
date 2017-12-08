from collections import Counter

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

--- Part Two ---

The programs explain the situation: they can't get down. Rather, they 
could get down, if they weren't expending all of their energy trying to 
keep the tower balanced. Apparently, one program has the wrong weight, 
and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms 
a sub-tower. Each of those sub-towers are supposed to be the same weight, 
or the disc itself isn't balanced. The weight of a tower is the sum of 
the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, 
gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its 
disc and all programs above it must each match. This means that the 
following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

As you can see, tknk's disc is unbalanced: ugml's stack is heavier than 
the other two. Even though the nodes above ugml are balanced, ugml itself 
is too heavy: it needs to be 8 units lighter for its stack to weigh 243 
and keep the towers balanced. If this change were made, its weight would 
be 60.

Given that exactly one program is the wrong weight, what would its weight 
need to be to balance the entire tower?
"""


def get_unbalanced_sub_node_correct_weight(puzzle_input):
    tree = build_tree(puzzle_input)
    unbalanced_sub_node_name = get_unbalanced_sub_node(tree)

    temp_tree = dict((node, (weight, sub_nodes)) for node, weight, sub_nodes in puzzle_input)

    node_to_weight = []
    for node in sibling_nodes(unbalanced_sub_node_name, puzzle_input):
        tree = build_tree_from_root(node[0], temp_tree)
        tree_weight = get_node_weight(tree)
        node_to_weight.append((node[0], tree_weight))

    weights_counter = Counter(w for _, w in node_to_weight)
    unbalanced_tree_weight, _ = weights_counter.most_common()[-1]
    unbalanced_node_weight = temp_tree[unbalanced_sub_node_name][0]

    balanced_tree_weight, _ = weights_counter.most_common()[0]
    balanced_node_weight = balanced_tree_weight - unbalanced_tree_weight + unbalanced_node_weight

    return unbalanced_sub_node_name, unbalanced_node_weight, balanced_node_weight


def get_unbalanced_sub_node(tree):
    node_name, sub_nodes = expand_node(tree)
    return _get_unbalanced_sub_node(node_name, sub_nodes)


def _get_unbalanced_sub_node(node_name, sub_nodes):
    sub_nodes_to_weight = [
        (sub_node, get_node_weight(sub_node)) for
        sub_node
        in sub_nodes
    ]
    weights_counter = Counter(w for _, w in sub_nodes_to_weight)

    if len(weights_counter) == 1:
        # sub_nodes are balanced! The offender is the current node.
        return node_name
    else:
        # I choose the sub_nodes with the different weight
        unbalanced_weight, _ = weights_counter.most_common()[-1]
        unbalanced_node = [n for n, w in sub_nodes_to_weight if w == unbalanced_weight][0]

        node_name, sub_nodes = expand_node(unbalanced_node)
        return _get_unbalanced_sub_node(node_name, sub_nodes)


def expand_node(node):
    node, (_, sub_nodes) = list(node.items())[0]
    return node, sub_nodes


def sibling_nodes(node_name, node_list):
    parent_node = [node for node in node_list if node_name in node[2]][0]
    return [node for node in node_list if node[0] in parent_node[2]]


def find_tree_root(rows):
    """ Tree root node is the one that is not child to any other node. """
    nodes = [n for n, w, s in rows]
    child_nodes = [ns for n, w, s in rows for ns in s]
    root_set = set(nodes) - set(child_nodes)
    return root_set.pop()


def build_tree(rows):
    """
    Starting from a list of (node_name, weight, sub_node_name) build a
    dict (node_name -> (weight, list[sub_nodes])); the output dict is recursive;
    sub_nodes have the same structure as the dict.
    """
    temp_tree = dict((node, (weight, sub_nodes)) for node, weight, sub_nodes in rows)
    root_node = find_tree_root(rows)
    return build_tree_from_root(root_node, temp_tree)


def build_tree_from_root(root, tree):
    weight, sub_nodes = tree[root]
    sub_tree = [build_tree_from_root(n, tree) for n in sub_nodes]

    return {root: (weight, sub_tree)}


def get_node_weight(tree):
    _, (weight, sub_nodes) = list(tree.items())[0]
    return weight + sum(get_node_weight(t) for t in sub_nodes)


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


if __name__ == '__main__':
    input_file = get_file_path('recursive_circus.txt')
    with open(input_file) as f:
        raw_puzzle_input = [line.strip() for line in f.readlines()]

    puzzle_input = parse_input(raw_puzzle_input)
    root_program = find_tree_root(puzzle_input)
    print(f'Result for Part 1: {root_program}')

    unbalanced_node, wrong_weight, correct_weight = get_unbalanced_sub_node_correct_weight(puzzle_input)
    print(f'Result for Part 2: node {unbalanced_node} has weight {wrong_weight}, should be {correct_weight}')
