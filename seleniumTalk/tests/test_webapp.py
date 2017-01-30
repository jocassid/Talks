
# Standard Library imports
from os.path import exists

# 3rd Party Libraries
from pytest import fixture
from selenium.webdriver import Ie, Firefox
from selenium.webdriver.support.ui import WebDriverWait

@fixture(scope='session')
def baseUrl(request):
    '''fixture to provide base URL'''
    return request.config.getoption('--baseurl')

@fixture(scope='session')
def driver(request):
    '''fixture function to instantiate webdriver'''
    browser = request.config.getoption('--browser').lower()
    if browser not in ['ie', 'firefox']:
        raise Exception('Invalid browser option %s' % browser)   
    
    if browser == 'firefox':
        firefoxExe = request.config.getoption('--firefoxbin')
        if not exists(firefoxExe):
            raise Exception('Firefox executable %s not found' % firefoxExe)   
    
    driver = None
    if browser == 'firefox':
        driver = Firefox(firefox_binary=firefoxExe)
    
    if browser == 'ie':
        # Force IEDriverServer.exe to use the default port
        driver = Ie(port=5555)

           
    driver.implicitly_wait(30)
    
    # yield statement turns this fixture function into a generator.  Since
    # this fixture is scoped to the module it gets called once when the module
    # starts.  Presumably at the end of the module the pytest framework calls
    # this fixture generator.  Since there are no more yields the cleanup 
    # portion runs.  This is awesome!
    yield driver
    
    # cleanup the driver
    driver.close()
    
    
def test_advancedSearch(driver, baseUrl):
    driver.get("%s/advanced_search" % baseUrl)
    
    # All these words field
    element = driver.find_element_by_id("_dKg")
    element.clear()
    element.send_keys("python podcast")
    
    # Language english
    driver.find_element_by_id('lr_button').click()
    WebDriverWait(driver, 20).until(
        lambda x: x.find_element_by_xpath("//li[@id=':d']/div")\
            .is_displayed())   
    driver.find_element_by_xpath("//li[@id=':d']/div").click()

    # click search
    WebDriverWait(driver, 20).until(
        lambda x: x.find_element_by_xpath("//input[@value='Advanced Search']")\
            .is_displayed())
    driver.find_element_by_xpath("//input[@value='Advanced Search']").click()
    
    element = driver.find_element_by_link_text("Talk Python To Me Podcast")
    assert "Talk Python To Me Podcast" == element.text
    
    
    
    
    
    
    
    





