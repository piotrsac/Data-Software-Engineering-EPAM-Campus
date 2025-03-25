def union(*args) -> set:
    """just a union join"""
    result = set()
    for arg in args:
        for item in arg:
            result.add(item)
    return result


def intersect(*args) -> set:
    """intersection join mad with usage of union, please don't look at it"""
    result = union(*args)
    un=union(*args)
    for arg in args:
        for item in un:
            if item not in arg:
                if item in result:
                    result.remove(item)
    return result



if __name__ == '__main__':
    assert union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']) == {'S', 'P', 'A', 'M', 'C'}
    assert intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')) == {'S', 'C'}
