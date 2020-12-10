__all__ = ['TestRailsKeywords']
__author__ = "Krishna Kaushik"
__version__ = "1.0"
__maintainer__ = "Krishna Kaushik"
__email__ = "tkrishnakaushik96@gmail.com"
__status__ = "Stagging"


from RF.components.testrail.HandleRequest import HandleRequest


class TestRailsKeywords:

    def test_rails_setup(self, url, user_name, password):
        self.hc = HandleRequest(url, user_name, password)

    def get_all_tests(self, run_id ):
        all_tests = self.hc.get_all_test(run_id)
        print(all_tests)

    def get_test(self, test_id):
        tests = self.hc.get_test(test_id)
        print(tests)
