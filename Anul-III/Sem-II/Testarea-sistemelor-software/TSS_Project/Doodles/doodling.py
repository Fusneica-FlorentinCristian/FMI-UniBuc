from inspect import getmembers, isfunction

from Tests import test_genetics

test_list = getmembers(test_genetics, isfunction)[1:]

print((test_list[0]))