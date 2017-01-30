
def pytest_addoption(parser):
    
    parser.addoption(
        '--baseurl',
        action='store',
        default='https://www.google.com',
        help='base url')
    
    parser.addoption(
        '--browser',
        action='store',
        default='firefox',
        help='browser: firefox or ie')
    
    # Location of Firefox executable.  This gets passed as an argument to
    # the Firefox driver constructor
    parser.addoption(
        '--firefoxbin',
        action='store',
        #default=r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe',
        default='/usr/bin/firefox',
        help='path of firefox executable (firefox.exe)')
    
    