try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
except:
    import os
    os.system('pip install selenium')
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

import time
import ctypes

def CreateProtonMail():
    driver = webdriver.Chrome()
    driver.get('https://10minutemail.net')
    global email, username
    name = ''
    emailElement = driver.find_element_by_id('fe_text')
    email = str(emailElement.get_attribute('value'))
    username = str(email.split('@')[0])

    print("[+] Email: " + email)
    print(f"[+] Username: {username}")
    
    driver.quit()

def CreateProtonVPN():
    driver = webdriver.Chrome()
    driver.get('https://mail.protonmail.com/create/new?language=en')

    ## JS click
##    element = driver.find_element_by_id('test')
##    driver.execute_script("arguments[0].click();", element)

    ## Make sure the iframe is loaded
    iframe = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,"#mainContainer > div > div > div.pm_panel.wide.signUpProcess-step-1.signupUserForm-container > form > div:nth-child(1) > div.usernameDomain-container > div > div > div.signupIframe-iframe > iframe"
            ))
        )

    ## Because the login form in another iframe, so need to switch to iframe first
    driver.switch_to.frame(iframe)

    ## Find element in a period of time after the web loaded
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "username")))
    time.sleep(0.1)
    element.send_keys(username)

    ## Switch back to default web
    driver.switch_to.default_content()

    element = driver.find_element_by_id("password")
    time.sleep(0.1)
    element.send_keys(email)

    element = driver.find_element_by_id("passwordc")
    time.sleep(0.1)
    element.send_keys(email)

    ## Switch to another iframe
    driver.switch_to.frame(driver.find_element_by_css_selector("#mainContainer > div > div > div.pm_panel.wide.signUpProcess-step-1.signupUserForm-container > form > div:nth-child(2) > section > div > div.signupIframe-iframe > iframe"))

    element = driver.find_element_by_id("notificationEmail")
    time.sleep(0.1)
    element.send_keys(email)

    element = driver.find_element_by_name('submitBtn')
    element.click()

def SaveCredential():
    try:
        f = open('ProtonMail.txt', 'a')
        f.write("Username: " + username + "\n")
        f.write("Password: " + email + '\n')
        f.write('------------------------------------------\n')
        f.close()
    except:
        with open('ProtonMail.txt', 'w') as f:
            f.write("Username: " + username + "\n")
            f.write("Password: " + email + '\n')
            f.write('------------------------------------------\n')
    

if __name__=="__main__":
    CreateProtonMail()
    CreateProtonVPN()
    ctypes.windll.user32.MessageBoxW(0, "Please verify CAPTCHA manually", "Information!", 0)
    ctypes.windll.user32.MessageBoxW(0, "After verifying CAPTCHA, please wait until it's DONE creating account", "Information!", 0)

    Ask = 0
    while True:
        Ask = ctypes.windll.user32.MessageBoxW(0, "Did you create a ProtonMail?", "Question?", 3)
        if (Ask == 6) or (Ask == 2):
            result = ctypes.windll.user32.MessageBoxW(0, "Are you sure?", "Confirm!", 4)
            if (result == 6) and (Ask == 6):
                SaveCredential()
                break
            elif (result == 6) and (Ask == 2):
                break
        if Ask == 7:
            ctypes.windll.user32.MessageBoxW(0, "Please finish it!", "Information", 0)
            
