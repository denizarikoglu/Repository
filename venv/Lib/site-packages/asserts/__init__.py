# -*- coding: utf-8 -*-


def sparse_check(pattern, obj, path=''):
    """Рекурсивно проверить, что `obj` повторяет структуру `pattern`.

    `pattern` должен "входить" в состав `obj`. Это значит, что:

    - списки в `obj` должны иметь те же элементы, что в `pattern`,
      но в любом порядке;
    - словари в `obj` должны иметь все ключи
      из соответствующих словарей в `pattern`
      (но могут содержать и другие);
    - прочие значения должны быть просто равны.

    Это удобно в тестах при проверке JSON-ответов от API.
    """

    if isinstance(pattern, dict):
        if not isinstance(obj, dict):
            raise AssertionError('{0} and {1} have different types at {2}'.format(pattern, obj, path))
        for key in pattern:
            sparse_check(pattern[key], obj.get(key), path=path + '[{0}]'.format(key))
    elif isinstance(pattern, list):
        if not isinstance(obj, list):
            raise AssertionError('{0} and {1} have different types at {2}'.format(pattern, obj, path))

        if len(obj) != len(pattern):
            raise AssertionError('{0} and {1} have different lengths {2} and {3} at {4}'.format(
                pattern, obj, len(pattern), len(obj), path))

        for idx, (pattern_elem, obj_elem) in enumerate(zip(pattern, obj)):
            sparse_check(pattern_elem, obj_elem, path=path + '[{0}]'.format(idx))

    else:
        assert pattern == obj, '{0} != {1} at {2}'.format(pattern, obj, path)

    return True
