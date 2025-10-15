volume_threshold = 1000000
dimensions_threshold = 150
weights_threshold = 20

standard_stack = "STANDARD"
special_stack = "SPECIAL"
rejected_stack = "REJECTED"

def sort(width, height, length, mass):
    # handle invalid input
    if width is None or height is None or length is None or mass is None:
        return None

    # check against the rule
    is_bulky = ((any([width, height, length]) >= volume_threshold or width * height * length >= volume_threshold)
                or width + height + length >= dimensions_threshold)
    is_heavy = mass >= weights_threshold

    if is_bulky and is_heavy:
        return rejected_stack
    elif not is_heavy and not is_bulky:
        return standard_stack
    else:
        return special_stack


if __name__ == '__main__':
    assert sort(10, 50, 100, 15) == special_stack


