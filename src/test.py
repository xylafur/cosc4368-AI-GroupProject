"""
    This is a testing module that is meant to be very generic.  The run_tests
    function will run any tests that exist in the TESTS list.  A test can be
    added to the TESTS list by using the 'test' decorator.

    All tests should exist in the "tests" directory and all of those modules
    must import both 'test' and 'TESTS' from this module.  Then as long as you
    use the decorator the magic happens ;)
"""

import os

TESTS = []

###############################################################################
#   Some Python magic ;)
###############################################################################
def test(func):
    """
        If a function uses the 'test' decorator (this outer fucntion) then it
        is automatically added to the TESTS list
    """
    TESTS.append(func)
    def inner(*args, **kwds):
        return func(*args, **kwds)

    return inner

def load_tests(test_dir="tests"):
    """
        Goes and imports all of the modules in the test_dir.  Any functions
        that were declared as tests using the test decorator are added to the
        TESTS list
    """
    global TESTS
    for f in os.listdir(test_dir):
        if f[-3:] == ".py":
            _temp = __import__(test_dir + "." + f[:-3], locals(), globals())
            # I had to do this because for some reason modifying the TESTS list
            # in the modules doesn't update it in this module.. so we have to
            # manually update it based on what it becomes in that module
            TESTS = eval("_temp.{}.TESTS".format(f[:-3]))

def run_tests(quiet=False, very_quiet=False):
    """
        Just goes an calls all of the functions in the TESTS list
        Anything that raises an exception is considered to fail, anything that
        doesn't is considered to pass.
    """
    if very_quiet:
        quiet = True

    fails = 0
    for test in TESTS:
        if not very_quiet:
            print("Running test {}".format(test.__name__))

        try:
            test()
        except Exception as e:
            if not very_quiet:
                print("Test {} failed!".format(test.__name__))

            if not quiet:
                print("Traceback below:")
                print(e)
            fails += 1

        else:
            if not quiet:
                print("Test {} passed!\n".format(test.__name__))

        test()

    if fails > 0:
        print("{} out of {} tests failed!".format(fails, len(TESTS)))
    else:
        print("No tests failed!")

if __name__ == '__main__':
    load_tests()
    run_tests()
