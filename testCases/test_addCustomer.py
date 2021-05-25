import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_002_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer *************")
        self.logger.info("************* Verifying Add Customer Page *************")

        self.driver = setup
        time.sleep(3)
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login Successful *************")
        self.logger.info("************* Starting add customer test *************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomersMenuItem()
        self.addcust.clickonAddnew()

        self.logger.info("************* Providing Customer info  *************")
        #print(str(self.random_generator()))
        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setGender("Female")
        self.addcust.setFirstname("Ravali")
        self.addcust.setLastname("Reddy")
        self.addcust.setDob("3/1/1985")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminComment("This is for testing...........")
        self.driver.execute_script("window.scrollBy(0,-1000)","")
        self.addcust.clickOnSave()

        self.logger.info("************* Saving Customer info *************")
        self.logger.info("************* Add customer Validation started *************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("************* Add Customer Test passed *************")
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_addCustomer_scr.png")
            self.logger.error("************* Add Customer test failed *************")
            assert True == False
        self.driver.close()
        self.logger.info("************* Ending Add Customer Title Test *************")


    def random_generator(len=8, chars=string.ascii_lowercase + string.digits):

        res = ''.join(random.choice(chars) for x in range(0,8))
        #print(res)
        return res

        #print("The Random String : " +str(res))
        #randomegen = ''.join(random.choice(chars) for x in range(size))

