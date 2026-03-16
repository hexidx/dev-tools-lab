from dev_tools_lab.line_count import count_lines


def test_count_lines_empty_text():
    assert count_lines("") == 0


def test_count_lines_single_line():
    assert count_lines("hello") == 1


def test_count_lines_multiple_lines():
    assert count_lines("a\nb\nc") == 3


def test_count_lines_trailing_newline_not_extra_line():
    assert count_lines("a\nb\n") == 2
