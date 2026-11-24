from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

# 1. Initialize the Chrome Driver
# Modern Selenium (v4.6+) automatically handles the driver executable for you
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#driver.implicitly_wait(30)
# 2. Open the URL
driver.get("http://103.27.234.18:8080/login.html")

# 3. Optional: Maximize the window so you can see everything
driver.maximize_window()

driver.find_element(By.XPATH,"(//*[@id='UserName'])[1]").send_keys("pawan.rai@feaindia.org")
time.sleep(3)
driver.find_element(By.XPATH,"(//*[@id='Password'])[1]").send_keys("Pawan@4747")
time.sleep(3)
driver.find_element(By.XPATH,"//*[text()='Login']").click()
time.sleep(3)
actions = ActionChains(driver)
webelement_student = driver.find_element(By.XPATH,"(//span[@class='k-link'])[6]")
actions.move_to_element(webelement_student).perform()
#
time.sleep(3)
web_student = driver.find_element(By.XPATH,"(//span[@class='k-icon k-i-arrow-e'])[2]")
actions.move_to_element(web_student).perform()


#month selection
time.sleep(3)
final_monthly = driver.find_element(By.XPATH,"(//a[@class='k-link'])[20]")
final_monthly.click()

# first select the dropdown which lists the options
time.sleep(2)
# select the all days of month
wait = WebDriverWait(driver, 30)
days = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='k-input'])[4]")))
days.click()
#wait for options to display so that All option is selected
options = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='session-list']/ul/li)[1]")))
options.click()
time.sleep(2)

# Click on the report type to select the LMS type
days = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='k-input'])[5]")))
days.click()
#wait for options to display so that LMS option is selected
options = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='reportType-list']/ul/li)[2]")))
options.click()
time.sleep(2)

time.sleep(3)
wait = WebDriverWait(driver, 10)
months = wait.until(EC.element_to_be_clickable((By.XPATH,"((//span[@class='k-select'])/span)[2]")))
months.click()
#driver.find_element(By.XPATH,"((//span[@class='k-select'])/span)[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"((//ul[@id='Month_listbox'])/li)[10]").click()

#Classroom PIN click on it so options appear
pin_op = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='k-icon k-i-arrow-s'])[9]")))
pin_op.click()

total_list_of_PINS = wait.until(EC.presence_of_all_elements_located((By.XPATH,"(//div[@id='CenterPIN-list']/ul/li)")))
print(len(total_list_of_PINS))
list_of_text = [pin.get_attribute('textContent') for pin in total_list_of_PINS]
list_of_not_clicked = []
for text in list_of_text:
    pin_op = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='k-icon k-i-arrow-s'])[9]")))
    pin_op.click()
    time.sleep(2)

    #options
    try:

        opt = wait.until(EC.element_to_be_clickable((By.XPATH,f"//div[@id='CenterPIN-list']//li[normalize-space()='{text}']")))
        opt.click()
        time.sleep(2)
        #click on reports one by one
        publish_report_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Get Report']")))
        publish_report_btn.click()
        time.sleep(5)
        #export_to_excel
        expt_excel = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Export To Excel']")))
        expt_excel.click()
        time.sleep(2)
        print("clicked for this text", text)
    except Exception as e:
        print(e)
        print("dint click on", text)
        list_of_not_clicked.append(text)

print(list_of_not_clicked)
time.sleep(4)
for text in list_of_not_clicked:
    for i in range(3):
        if text != "--Select--":
            pin_op = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='k-icon k-i-arrow-s'])[9]")))
            pin_op.click()
            time.sleep(2)

            # options
            opt = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[@id='CenterPIN-list']//li[normalize-space()='{text}']")))
            opt.click()
            time.sleep(2)
            # click on reports one by one
            publish_report_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Get Report']")))
            publish_report_btn.click()
            time.sleep(5)
            # export_to_excel
            expt_excel = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Export To Excel']")))
            expt_excel.click()
            time.sleep(12)
            print(f"clicked for this {text} on {i}th attempt")


# 5. Close the browser session
driver.quit()