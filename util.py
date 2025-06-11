def read_lines_from_file(filename):
    with open(filename) as f:
        return f.readlines()

def read_whole_file(filename):
    with open(filename) as f:
        return f.read()


def transpose_2d_list(lines):
    return None