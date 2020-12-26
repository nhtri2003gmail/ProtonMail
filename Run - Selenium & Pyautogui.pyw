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
try:
    import pyautogui
except:
    import os
    os.system('pip install pyautogui')
    import pyautogui

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
    while True:
        usernamePos = pyautogui.locateCenterOnScreen('Images\\Username.png')
        if usernamePos != None:
            break
        time.sleep(0.1)
    pyautogui.moveTo(usernamePos, duration=0.5)
    pyautogui.click()
    pyautogui.write(username)
    
    time.sleep(0.5)
    pyautogui.scroll(-380)
    time.sleep(0.5)
    
    passwordPos = pyautogui.locateCenterOnScreen('Images\\Password.png')
    pyautogui.moveTo(passwordPos, duration=0.5)
    pyautogui.click()
    pyautogui.write(email)
    
    passwordConfirmPos = pyautogui.locateCenterOnScreen('Images\\Confirm_Password.png')
    pyautogui.moveTo(passwordConfirmPos, duration=0.5)
    pyautogui.click()
    pyautogui.write(email)
    
    recoveryEmailPos = pyautogui.locateCenterOnScreen('Images\\Recovery_Email.png')
    pyautogui.moveTo(recoveryEmailPos, duration=0.5)
    pyautogui.click()
    pyautogui.write(email)
    
    time.sleep(0.5)
    pyautogui.scroll(-300)
    time.sleep(0.5)

    createAccountPos = pyautogui.locateCenterOnScreen('Images\\Create_Account.png')
    pyautogui.moveTo(createAccountPos, duration=0.5)
    pyautogui.click()

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
    ctypes.windll.user32.MessageBoxW(0, "You cannot touch mouse or keyboard after press OK\n\nWhen there is a CAPTCHA, you can use your mouse and keyboard", "Information!", 0)
    
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
            


