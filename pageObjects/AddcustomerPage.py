import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class AddCustomer:
    linkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtlastname_xpath = "//input[@id='LastName']"
    txtcustomRoles_xpath = "(//div[contains(@class,'k-multiselect-wrap')])[2]"
    lstitem_Administrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitem_Moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitem_Guests_xpath = "//li[contains(text(),'Guests')]"
    lstitem_Registered_xpath = "//li[contains(text(),'Registered')]"
    lstunselect_Registered_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    lstitem_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    drpMgrofVendor_xpath = "//select[@id='VendorId']"
    selectvendor1_xpath = "//select[@id='VendorId']/option[@value='1']"
    selectvendor2_xpath = "//select[@id='VendorId']/option[@value='2']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFeMaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyname_xpath = "//input[@id='Company']"
    chkboxTaxexempt_xpath = "//input[@id='IsTaxExempt']"
    txtadmin_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menu_xpath).click()

    def clickonCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menuitem_xpath).click()

    def clickonCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element_by_xpath(self.txtlastname_xpath).send_keys(lastname)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomRoles_xpath).click()
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Administrators_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Moderators_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lstunselect_Registered_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)
            self.driver.execute_script("arguments[0].click;",self.listitem)

    def setManagerofVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpMgrofVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender=="Female":
            self.driver.find_element_by_xpath(self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)
    def setCompanyName(self,compname):
        self.driver.find_element_by_xpath(self.txtCompanyname_xpath).send_keys(compname)
    def setAdminComment(self,comment):
        self.driver.find_element_by_xpath(self.txtadmin_xpath).send_keys(comment)
    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()


