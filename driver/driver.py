import os
from appium import webdriver


class DriverBuilder(object):

    def __init__(self, platform='Android', version='', device_name='emulator-5554'):
        apk = r'{}\Restaurante America\app\android-release.apk'.format(os.path.dirname(os.getcwd()))
        desired_capabilities = {
            'noReset': True,
            'platformName': platform,
            'platformVersion': version,
            'deviceName': device_name,
            'app': apk,
            'appPackage': 'br.com.americaburger.app',
            'appActivity': '.MainActivity',
            'gpsEnabled':True,
            'dontStopAppOnReset':True,
            'avd':'X86'
        }
        server = 'http://127.0.0.1:4723/wd/hub'
        self.driver = webdriver.Remote(server, desired_capabilities)

    def get_driver(self):
        return self.driver

    def end(self):
        self.driver.quit()