def count_lines(filepath):
    with open(filepath, 'r+') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(filepath):
    with open(filepath) as f:
        contents = f.read()
        length = len(contents)
        return length


def test(name):
    print("Number of lines is:", count_lines(name))
    print("Number of characters is:", count_chars(name))
