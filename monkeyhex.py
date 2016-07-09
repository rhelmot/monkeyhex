def maybe_hex(item, list_depth=0):
    if isinstance(item, bool):
        return repr(item)
    if isinstance(item, (int, long)):
        return hex(item)
    elif isinstance(item, (list,)):
        return '[%s]' % joinlist(item, list_depth + 1)
    elif isinstance(item, (set,)):
        return '{%s}' % joinlist(item, list_depth + 1)
    elif isinstance(item, (dict,)):
        return '{%s}' % joindict(item, list_depth + 1)
    elif isinstance(item, (tuple,)):
        return '(%s)' % joinlist(item, list_depth + 1)
    else:
        return repr(item)

def get_joiner(lst, list_depth):
    joiner = ',\n' if len(repr(lst)) > 80 and len(lst) < 400 else ', '
    if joiner[1] == '\n':
        joiner += ' '*list_depth
    return joiner

def joinlist(lst, list_depth):
    return get_joiner(lst, list_depth).join(maybe_hex(a, list_depth) for a in lst)

def joindict(dct, list_depth):
    return get_joiner(dct, list_depth).join(
        '%s: %s' % (maybe_hex(key, list_depth), maybe_hex(val, list_depth))
                for key, val in dct.iteritems()
    )

def hex_print(item):
    if type(item) is bool:
        old_display_hook(item)
        return
    elif item is None:
        old_display_hook(item)
        return

    representation = maybe_hex(item)
    try:
        class hexprinted(type(item)):
            def __init__(self, qqq):
                self.__qqq = qqq
                super(hexprinted, self).__init__(qqq)

            def __repr__(self):
                return maybe_hex(item)
        old_display_hook(hexprinted(item))
    except:
        old_display_hook(item)

ipython = False
import inspect
for frame in inspect.stack():
    if 'IPython' in frame[1]:
        ipython = True

if ipython:
    import IPython
    formatter = IPython.get_ipython().display_formatter.formatters['text/plain']
    formatter.for_type(int, lambda n, p, cycle: p.text(hex(n)))
else:
    import sys
    old_display_hook = sys.displayhook
    sys.displayhook = hex_print
