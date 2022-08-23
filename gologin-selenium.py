import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from gologin import GoLogin
from gologin import get_random_port

random_port = get_random_port()

gl = GoLogin({
	# add Token of your system's GoLogin below by going to settings>Api Documentation>Create new Token and paste.
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmZkZmM5YWQ3OTJkNzViNGMyYjc5MjEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MmZkZmY1OGRkZjZhNDNkZDY2NDc5MDkifQ.7iDdhqyTvLXJWt0e2hu5mjvvnrFQShgckdyC3pSPxEc",

	# After creating new Profile for the store,click on option of the profile and copy Id and paste Below
	"profile_id": "62fdfc9ad792d7e8012b7923",
	"port": random_port
	})

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	# Below Path of the chromedriver.exe needs to be pasted where it is located on your system in the saks-SeleniumAutomation directory.
	chrome_driver_path = "C:/Users/saksh/Documents/saks-SeleniumAutomation/chromedriver_win32/chromedriver.exe"

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.maximize_window()
# get request to locate shopify 1mbb
driver.get("https://www.shopify.com/1mbb")
time.sleep(5)
driver.find_element_by_xpath("//*[text()='Start free trial']").click()
driver.find_element_by_xpath("//*[text()='Yes']").click()
driver.find_element_by_name("commit").click()




# <------- Enter the Gmail created for Store,Password and store name in Specified Filed-------->
driver.find_element_by_name("signup[email]").send_keys("fbfwrb@gmail.com")
driver.find_element_by_name("signup[password]").send_keys("fuebfusdb@gmail.com")
driver.find_element_by_name("signup[shop_name]").send_keys("something test36")
driver.find_element_by_xpath("//*[text()='Create your store']").click()
time.sleep(15)

driver.find_element_by_xpath("//*[text()='Skip']").click()
driver.find_element_by_xpath("//*[text()='Next']").click()
time.sleep(8)
sel = Select(driver.find_element_by_xpath("//select[@name='account_setup[country]']"))
sel.select_by_value("US")
driver.find_element_by_xpath("//*[text()='Enter my store']").click()
time.sleep(30)
driver.find_element_by_xpath("//*[text()='Finances']").click()
time.sleep(8)
driver.find_element_by_xpath("//*[text()='Billing']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[text()='Your trial just started']").click()
time.sleep(15)
driver.find_element_by_xpath("//*[text()='Change currency']").click()
driver.find_element_by_xpath("//*[text()='Save']").click()
time.sleep(15)
driver.find_element_by_xpath("//*[text()='Your trial just started']").click()
driver.find_element_by_xpath("//*[text()='Select a plan']").click()
driver.find_element_by_xpath("//div*[@aria-label='Choose this plan']").click()

