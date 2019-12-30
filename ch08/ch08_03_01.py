import functools

enumerate1 = functools.partial(enumerate, start=1)
for lion, line in enumerate1(lines):
    process_line(lion, line)


reader = functools.partial(open, mode='rt', encoding='utf8')
writer = functools.partial(open, mode='wt', encoding='utf8')


def reader2(filename, mode='rt', encoding='utf8', *args, **kwargs):
    return open(filename, mode=mode, encoding=encoding, *args, **kwargs)


def writer2(filename, mode='wt', encoding='utf8', *args, **kwargs):
    return open(filename, mode=mode, encoding=encoding, *args, **kwargs)
