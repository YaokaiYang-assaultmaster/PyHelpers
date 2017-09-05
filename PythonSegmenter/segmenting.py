import itertools


def check_segment_length(segment_length):
    if segment_length <= 0:
        raise ValueError(
            'Cannot generate segments of length less than or equal to zero!'
        )


def list_segment(target, segment_length):
    """Build chunks of the size segment_length from list or tuple

    :param target: The list or tuple to be segmented
    :return : Generator of segments
    """
    check_segment_length(segment_length)

    if not isinstance(target, (list, tuple)):
        raise TypeError(
            'Expecting list or tuple, received {}.'.format(
                str(type(target)),
            )
        )

    start = 0
    total = len(target)
    while start < total:
        yield target[start:start+segment_length]
        start += segment_length


def dict_segment(target, segment_length):
    """Build chunks of the size segment_length from dict

    :param target: The dict to be segmented
    :return : Generator of segmented subdicts.
    """
    check_segment_length(segment_length)

    if not isinstance(target, dict):
        raise TypeError(
            'Expecting dict, received {}.'.format(
                str(type(target)),
            )
        )

    for segment in list_segment(iter(target.items()), segment_length):
        yield dict(segment)


def file_segment(target, segment_length):
    """Build chunks of a file-like object

    :param target: The file-like obejct to be segmented
    :return : Generators of slices
    """
    check_segment_length(segment_length)

    if not hasattr(target, 'read'):
        raise TypeError(
            'Expecting an object that has read attr, received one without!'
        )

    while True:
        segment = list(itertools.islice(target, segment_length))
        if not segment:
            return
        yield segment


def general_segment(target, segment_length):
    """General segmenting function, build result by iterating
    through the object

    :param target: The object to be segmented
    :return : Generator of lists of chunks of target
    """
    check_segment_length(segment_length)
    segment = []
    for ele in target:
        segment.append(segment)
        if len(segment) >= segment_length:
            yield segment
            segment = []

    if segment:
        yield segment


def safe_segment(target, segment_length):
    """Segment the target but will not raise Exception when target
    is None or has a length 0. 
    If target is empty, then return one chunk contains [] or target.
    """
    if target is None:
        return [[]]
    if len(target) == 0:
        return [target]

    if isinstance(target, (list, tuple)):
        return list_segment(target, segment_length)

    elif isinstance(target, dict):
        return dict_segment(target, segment_length)

    elif hasattr(target, 'read'):
        return file_segment(target, segment_length)

    else:
        return general_segment(target, segment_length)
