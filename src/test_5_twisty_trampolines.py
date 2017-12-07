from src.aoc_5_twisty_trampolines import steps_to_reach_exit, compute_next_step_part_1, compute_next_step_part_2


def test_sample_part_1():
    offsets = [0, 3, 0, 1, -3]
    expected_steps = 5

    actual_steps, _ = steps_to_reach_exit(offsets, next_step=compute_next_step_part_1)
    assert actual_steps == expected_steps


def test_sample_part_2():
    offsets = [0, 3, 0, 1, -3]
    expected_steps = 10
    expected_final_instructions = [2, 3, 2, 3, -1]

    actual_steps, final_instructions = steps_to_reach_exit(offsets, next_step=compute_next_step_part_2)
    assert actual_steps == expected_steps
    assert final_instructions == expected_final_instructions
