from itertools import cycle, chain, count
from sys import setrecursionlimit
from typing import Tuple, Union, List, Iterator

import itertools

from src.utils import read_lines, head

"""
--- Day 13: Packet Scanners ---

You need to cross a vast firewall. The firewall consists of several layers,
each with a security scanner that moves back and forth across the layer. To
succeed, you must not be detected by a scanner.

By studying the firewall briefly, you are able to record (in your puzzle
input) the depth of each layer and the range of the scanning area for the
scanner within it, written as depth: range. Each layer has a thickness of
exactly 1. A layer at depth 0 begins immediately inside the firewall; a
layer at depth 1 would start immediately after that.

For example, suppose you've recorded the following:

0: 3
1: 2
4: 4
6: 4

This means that there is a layer immediately inside the firewall (with
range 3), a second layer immediately after that (with range 2), a third
layer which begins at depth 4 (with range 4), and a fourth layer which
begins at depth 6 (also with range 4). Visually, it might look like this:

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Within each layer, a security scanner moves back and forth within its
range. Each security scanner starts at the top and moves down until it
reaches the bottom, then moves up until it reaches the top, and repeats. A
security scanner takes one picosecond to move one step. Drawing scanners as
S, the first few picoseconds look like this:

Picosecond 0:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 1:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

Your plan is to hitch a ride on a packet about to move through the
firewall. The packet will travel along the top of each layer, and it moves
at one layer per picosecond. Each picosecond, the packet moves one layer
forward (its first move takes it into layer 0), and then the scanners move
one step. If there is a scanner at the top of the layer as your packet
enters it, you are caught. (If a scanner moves into the top of its layer
while you are there, you are not caught: it doesn't have time to notice you
before you leave.) If you were to do this in the configuration above,
marking your current position with parentheses, your passage through the
firewall would look like this:

Initial state:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 0:
 0   1   2   3   4   5   6
(S) [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
( ) [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 1:
 0   1   2   3   4   5   6
[ ] ( ) ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] (S) ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]


Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] (.) ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] (.) ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]


Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... (.) [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

 0   1   2   3   4   5   6
[S] [S] ... (.) [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]


Picosecond 4:
 0   1   2   3   4   5   6
[S] [S] ... ... ( ) ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... ( ) ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 5:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] (.) [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [S] ... ... [S] (.) [S]
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]


Picosecond 6:
 0   1   2   3   4   5   6
[ ] [S] ... ... [S] ... (S)
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... ( )
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]
In this situation, you are caught in layers 0 and 6, because your packet
entered the layer when its scanner was at the top when you entered it. You
are not caught in layer 1, since the scanner moved into the top of the
layer once you were already there.

The severity of getting caught on a layer is equal to its depth multiplied
by its range. (Ignore layers in which you do not get caught.) The severity
of the whole trip is the sum of these values. In the example above, the
trip severity is 0*3 + 6*4 = 24.

Given the details of the firewall you've recorded, if you leave immediately,
what is the severity of your whole trip?
"""

# A layer is described by a tuple composed by:
#  - An integer, representing the depth of the layer
#  - Another integer, representing the range of the layer
#  - A generator, wich returns the next position of the scanner each
#    time next() is called on it
Layer = Tuple[int, int, Iterator[int]]
Layers = List[Union[Layer, None]]


def compute_cost(layers, n_layer):
    if not layers:
        return 0

    current_layer, other_layers = head(layers)

    layer_severity = 0
    if current_layer is not None:
        scanner_position, _ = tick_layer(current_layer)

        if scanner_position == 0:
            d, r, _ = current_layer
            layer_severity = d * r

            if layer_severity != 0:
                print(n_layer, r)
                return layer_severity

    other_layers = [tick_layer(l)[1] for l in other_layers]
    return layer_severity + compute_cost(other_layers, n_layer+1)


def get_ps_delay(puzzle_input):
    for delay in count(3000, step=2):
        tweaked_firewall_structure = ([None] * delay) + compose_firewall_structure(puzzle_input)
        #print(len(tweaked_firewall_structure), end=' ')
        cost = compute_cost(tweaked_firewall_structure, 0)

        #print(f'{delay} -> {cost}')

        if cost == 0:
            return delay


def tick_layer(layer: Layer) -> Tuple[int, Layer]:
    next_scanner_position = None
    if layer is not None:
        _depth, _range, scanner_position = layer
        next_scanner_position = next(scanner_position)
    return next_scanner_position, layer


def compose_firewall_structure(layer_configuration):
    max_layer = max(layer_configuration.keys())

    return [
        (
            depth,
            layer_configuration[depth],
            layer_gen(layer_configuration[depth])
        ) if depth in layer_configuration else None
        for depth in range(max_layer + 1)
    ]


def layer_gen(layer_range):
    # return an iterator that return int from 0 to range and back
    return cycle(chain(range(layer_range), reversed(range(1, layer_range - 1))))


def parse_layer_configuration(raw_puzzle_input):
    return dict(parse_row(r) for r in raw_puzzle_input)


def parse_row(row):
    depth, scanner_range = row.split(':')
    return int(depth.strip()), int(scanner_range.strip())


if __name__ == '__main__':
    setrecursionlimit(5000)
    #puzzle_input = parse_layer_configuration(read_lines('packet_scanners.txt'))
    #firewall_structure = compose_firewall_structure(puzzle_input)
    #cost = compute_cost(firewall_structure)
    #print(f'Result for Part 1: {cost}')

    #delay = get_ps_delay(puzzle_input)
    #print(f'Result for Part 2: {delay}')