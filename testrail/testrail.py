from testrail.api_client import APIClient
from testrail.testrail_config import (
    USER,
    PWD,
    URL,
    PROJECT_ID,
    CASE_TYPE_TO_ID)


class TestRailAgent():
    def __init__(self):
        self.client = APIClient(URL)
        self.client.user = USER
        self.client.password = PWD

    def get_case(self, tid):
        """ get test case by id"""
        return self.client.send_get('get_case/%d' % int(tid))

    def get_run(self, rid):
        """ get a test run by its id"""
        return self.client.send_get('get_run/%d' % int(rid))

    def add_run(self, name, description='', milestone=None, assignedTo=None,
                include_all=False, case_ids=None):
        """ add test run based on parameters
            milestone: int
            assignedTo: int
            case_ids: list
        """
        if not case_ids:
            case_ids = []

        data = {
            'name': name,
            'description': description,
            'milestone_id': milestone,
            'assignedto_id': assignedTo,
            'include_all': include_all,
            'case_ids': case_ids
        }
        return self.client.send_post('add_run/%d' % PROJECT_ID, data)

    def get_tests(self, rid):
        """ get tests in a test run"""
        return self.client.send_get('get_tests/%d' % int(rid))

    def get_case_types(self):
        """ get available case type mapping"""
        return self.client.send_get('get_case_types')

    def get_cases_by_type(self, test_type):
        """ get all cases for a certain type"""
        assert test_type in CASE_TYPE_TO_ID
        return self.client.send_get('get_cases/%d&type_id=%d' %
                                    (PROJECT_ID, CASE_TYPE_TO_ID[test_type]))

    def add_results(self, rid, results):
        return self.client.send_post('add_results/%d' % rid, results)

    def add_attachment(self, rsid, attachment):
        return self.client.send_post('add_attachment_to_result/%d' % rsid, attachment)


if __name__ == '__main__':
    """ test TestRailAgent
    """
    agent = TestRailAgent()

    # try:
    #     print agent.get_case_types()
    #     print 'get_case_types pass!'
    # except:
    #     print 'get_case_types fail!'

    # try:
    #     print agent.get_case(554)
    #     print 'get_case pass!'
    # except:
    #     print 'get_case fail!'

    # try:
    #     agent.get_cases_by_type('Other')
    #     print 'get_cases_by_type pass!'
    # except Exception, e:
    #     print 'get_cases_by_type fail!'

    # try:
    #     print agent.get_run(4104)
    #     print 'get_run pass!'
    # except:
    #     print 'get_run fail!'

    # try:
    #     print agent.get_tests(4104)
    #     print 'get_tests pass!'
    # except Exception, e:
    #     print 'get_tests fail!'

    # try:
    #     print agent.add_run('Test TestRailAgent')
    #     print 'add_run pass!'
    # except:
    #     print 'add_run fail!'
