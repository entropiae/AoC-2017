from src.utils import get_file_path, head
from sys import setrecursionlimit

"""
--- Day 9: Stream Processing ---

A large stream blocks your path. According to the locals, it's not safe
to cross the stream at the moment because it's full of garbage. You look
down at the stream; rather than water, you discover that it's a stream of
characters.

You sit for a while and record part of the stream (your puzzle input).
The characters represent groups - sequences that begin with { and end
with }. Within a group, there are zero or more other things, separated by
commas: either another group or garbage. Since groups can contain other
groups, a } only closes the most-recently-opened unclosed group - that
is, they are nestable. Your puzzle input represents a single, large group
which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. Garbage begins with
< and ends with >. Between those angle brackets, almost any character can
appear, including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, some program has canceled
some of the characters within it using !: inside garbage, any character
that comes after ! should be ignored, including <, >, and even another !.

You don't see any characters that deviate from these rules. Outside
garbage, you only find well-formed groups, and garbage always terminates
according to the rules above.

Here are some self-contained pieces of garbage:

 - <>, empty garbage.
 - <random characters>, garbage containing random characters.
 - <<<<>, because the extra < are ignored.
 - <{!>}>, because the first > is canceled.
 - <!!>, because the second ! is canceled, allowing the > to terminate
   the garbage.
 - <!!!>>, because the second ! and the first > are canceled.
 - <{o"i!a,<{i<a>, which ends at the first >.

Here are some examples of whole streams and the number of groups they contain:

 - {}, 1 group.
 - {{{}}}, 3 groups.
 - {{},{}}, also 3 groups.
 - {{{},{},{{}}}}, 6 groups.
 - {<{},{},{{}}>}, 1 group (which itself contains garbage).
 - {<a>,<a>,<a>,<a>}, 1 group.
 - {{<a>},{<a>},{<a>},{<a>}}, 5 groups.
 - {{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are
   canceled).

Your goal is to find the total score for all groups in your input. Each
group is assigned a score which is one more than the score of the group
that immediately contains it. (The outermost group gets a score of 1.)

 - {}, score of 1.
 - {{{}}}, score of 1 + 2 + 3 = 6.
 - {{},{}}, score of 1 + 2 + 2 = 5.
 - {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
 - {<a>,<a>,<a>,<a>}, score of 1.
 - {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
 - {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
 - {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.

What is the total score for all groups in your input?

--- Part Two ---

Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters
within the garbage. The leading and trailing < and > don't count, nor do 
any canceled characters or the ! doing the canceling.

 - <>, 0 characters.
 - <random characters>, 17 characters.
 - <<<<>, 3 characters.
 - <{!>}>, 2 characters.
 - <!!>, 0 characters.
 - <!!!>>, 0 characters.
 - <{o"i!a,<{i<a>, 10 characters.

How many non-canceled characters are within the garbage in your puzzle 
input?
"""


def count_groups(puzzle_input):
    return count(filter_garbage(filter_deletions(puzzle_input)))


def count(stream):
    return _do_count(list(stream), 0, 0)


def _do_count(stream, acc, unbalanced_groups_count):
    if not stream:
        return acc

    h, t = head(stream)

    if h == '{':
        unbalanced_groups_count += 1
    elif h == '}':
        acc += unbalanced_groups_count
        unbalanced_groups_count -= 1

    return _do_count(t, acc, unbalanced_groups_count)


def filter_deletions(stream):
    """
    Remove deletions from the stream
    """
    is_deleted = False

    for c in stream:
        if is_deleted:
            is_deleted = False
            continue
        if c == '!':
            is_deleted = True
            continue
        yield c


def filter_garbage(stream):
    """
    Remove garbage group from the stream
    """
    is_garbage = False
    for c in stream:
        if c == '>':
            is_garbage = False
            continue
        if c == '<':
            is_garbage = True
            continue
        if is_garbage:
            continue
        yield c


def filter_comma(stream):
    for c in stream:
        if c == ',':
            continue
        yield c


def count_garbage(puzzle_input):
    return _count_garbage(filter_deletions(puzzle_input))


def _count_garbage(stream):
    is_garbage = False
    counter = 0
    for c in stream:
        if c == '>':
            is_garbage = False
            continue
        if c == '<':
            if is_garbage:
                counter += 1
            is_garbage = True
            continue
        if is_garbage:
            counter += 1
    return counter


if __name__ == '__main__':
    # Avoid RecursionError with the default limit (1000)
    setrecursionlimit(5000)

    file_path = get_file_path('stream_processing.txt')

    with open(file_path) as f:
        puzzle_input = f.readline().strip()

    group_n = count_groups(puzzle_input)
    print(f'Result for Part 1: {group_n}')

    garbage_count = count_garbage(puzzle_input)
    print(f'Result for Part 2: {garbage_count}')
