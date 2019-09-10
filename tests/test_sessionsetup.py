import session-setup  # need to figure out how to use __init__.py ???
import unittest

class TestOS(unittest.TestCase):
    """ Test the add function from the mymath library. """

        def test_host_os(self):
        """ Test the return of the host system operating system.  """

        result = sessionsetup.this_host()
        self.assertEqual(result, 'Darwin')
 
if __name__ == '__main__':
    unittest.main()