"""Line counting utility helpers."""


def count_lines(text: str) -> int:
    """Return the number of lines in *text*.

    Empty text returns 0. A trailing newline does not create an extra line.
    """
    if text == "":
        return 0

    return len(text.splitlines())
