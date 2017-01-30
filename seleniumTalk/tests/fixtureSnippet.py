
# 3rd Party Libraries
from pytest import fixture

CUSTOMER_IDS = {
    'http://devserver':'10823',
    'http://testserver':'20939'
}

@fixture(scope='function')
def customerID(baseUrl):
    customerID = CUSTOMER_IDS.get(baseUrl, None)
    if customerID is None:
        raise Exception("No customerID found for %s" % baseUrl)
    return customerID
    




