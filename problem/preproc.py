def read_input(file_name):
    """

    :param file_name:
    :return: dictionary where each employee has a list of skills
    """
    empl = {}
    input_file = open(file_name)
    for line in input_file:
        line = line.strip('\n').split(' ')
        empl[line[0]] = line[1:]
    return empl


def skills_to_nr(skills):
    """
    Each list of skills can be characterized by a bit mask

    :param skills:
    :return: hash number of skill list
    """
    ret = 0
    for skill in skills:
        p = ord(skill) - ord('a')
        ret += (1 << p)
    return ret


def has_skills(source, target):
    return source & target
