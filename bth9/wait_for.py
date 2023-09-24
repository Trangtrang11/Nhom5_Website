from venv import logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class wait_for:
    def wait_for_exists_by_xpath(self, driver, x_path, time_out=0):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.XPATH, x_path)))
            return True
        except:
            logger.info('Cannot find element: %s' %str(x_path))
            self.print_exception()
            return False

    def wait_for_exists_by_css(self, driver, css_selector, time_out):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
            return True
        except:
            logger.info('Cannot find element: %s' %str(css_selector))
            self.print_exception()
            return False

    def wait_for_exists_by_name(self, driver, name, time_out=0):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.NAME, name)))
            return True
        except:
            logger.info('Cannot find element: %s' %str(name))
            self.print_exception()
            return False
    def wait_for_exists_by_class_name(self, driver, classname, time_out=0):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located(By.CLASS_NAME, classname))
            return True
        except:
            logger.info('Cannot find element: %s' %str(classname))
            self.print_exception()
            return False
    
    def send_keys(self, driver, message):
        try:
            message = str(message)
            data = message.split(':')
            a = 0
            while a < len(data):
                ActionChains(driver).send_keys(data[a]).perform()
                a = a + 1
                if a < len(data):
                    ActionChains(driver).key_down(Keys.SHIFT).send_keys(";").key_up(Keys.SHIFT).perform()
            return True
        except:
            logger.info('Cannot send keys: %s' %str(message))
            self.print_exception()
            return False
        
    def click_element_by_xpath(self, driver, xpath):
        try:
            driver.find_element(By.XPATH, xpath).click()
            logger.info('Clicked element %s' % xpath)
            return True
        except:
            logger.info('Cannot click: %s' %str(xpath))
            self.print_exception()
            return False
            
    def send_key_enter(self, driver):
        try:
            ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            logger.info("Pressed enter")
            return True
        except:
            self.print_exception()
            return False
    
    def wait_and_sendkeys_by_xpath(self, driver, xpath, keys, time_out=10):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(keys)
            return True
        except:
            logger.info('Element is not wait and click: %s' %[xpath, keys])
            self.print_exception()
            return False

    def wait_and_sendkeys_by_css(self, driver, css_selector, keys, time_out=20):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))).send_keys(keys)
            return True
        except:
            logger.info('Element is not wait and send keys: %s' %[css_selector, keys])
            self.print_exception()
            return False

    def wait_and_sendkeys_by_id(self, driver, id, keys, time_out=10):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.ID, id))).send_keys(keys)
            return True
        except:
            logger.info('Element is not wait and send keys: %s' %[id, keys])
            self.print_exception()
            return False
        
    def wait_and_click_by_xpath(self, driver, xpath, time_out=10):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
            return True
        except:
            logger.info('Element is not wait and click with xpath: %s' %str(xpath))
            self.print_exception()
            return False

    def wait_and_click_by_css(self, driver, css_selector, time_out=10):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))).click()
            return True
        except:
            logger.info('Element is not wait and click: %s' %str(css_selector))
            self.print_exception()
            return False

    def wait_and_click_by_id(self, driver, ids, time_out=10):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.ID, ids))).click()
            return True
        except:
            logger.info('Element is not wait and click: %s' %str(ids))
            self.print_exception()
            return False

    def wait_and_click_by_name(self, driver, name, time_out=10):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.NAME, name))).click()
            return True
        except:
            logger.info('Element is not wait and click with name: %s' %str(name))
            self.print_exception()
            return False

    def wait_and_click_by_class_name(self, driver, class_name, time_out=10):
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name))).click()
            return True
        except:
            logger.info('Element is not wait and click: %s' %str(class_name))
            self.print_exception()
            return False