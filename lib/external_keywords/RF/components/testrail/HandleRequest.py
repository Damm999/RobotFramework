from testrail_api import TestRailAPI

__all__ = ['HandleRequest']
__author__ = "Krishna Kaushik"
__version__ = "1.0"
__maintainer__ = "Krishna Kaushik"
__email__ = "tkrishnakaushik96@gmail.com"
__status__ = "Stagging"


class HandleRequest:

    def __init__(self, url, user_name, password):
        self.api = TestRailAPI(url, user_name, password)

    def get_all_test(self, run_id):
        tests = self.api.tests
        return tests.get_tests(run_id)

    def get_test(self, test_id):
        tests = self.api.tests
        return tests.get_test(test_id)

