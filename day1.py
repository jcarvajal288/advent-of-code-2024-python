def read_lines_from_file(filename):
    with open(filename) as f:
        return f.readlines()

def total_distance_between_lists(filename):
    splits = [x.split(' ') for x in read_lines_from_file(filename)]
    left_side = sorted([int(x[0]) for x in splits])
    right_side = sorted([int(x[-1]) for x in splits])
    differences = [abs(x[1] - x[0]) for x in zip(left_side, right_side)]
    return sum(differences)


def similarity_score(filename):
    splits = [x.split(' ') for x in read_lines_from_file(filename)]
    left_side = sorted([int(x[0]) for x in splits])
    right_side = sorted([int(x[-1]) for x in splits])
    similarity_scores = [right_side.count(x) * x for x in left_side]
    return sum(similarity_scores)
        
