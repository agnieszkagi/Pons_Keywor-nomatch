import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()
# browser.get("https://pl.pons.com/t%C5%82umaczenie?q=&l=frpl&in=&lf=fr&qnac=")

# disable cookies:
ops = options()
ops.set_preference("network.cookie.cookieBehavior", 2)
browser = webdriver.Firefox(options=ops)
try:
    browser.get("https://pl.pons.com/t%C5%82umaczenie?q=&l=frpl&in=&lf=fr&qnac=")
except Exception as exc:
    print("There was a problem: %s" % (exc))

input_elem = browser.find_element_by_id("q")
input_elem.clear()

#keyword list to be checked

input_elem.send_keys(keyword)
input_elem.send_keys(Keys.RETURN)
time.sleep(3)
1=0
Final_list =[]

if "fuzzysearch" in browser.page_source:
    Final_list.append(keyword)
    i +=1


# browser.close()
"""
fp = webdriver.FirefoxProfile()
fp.set_preference("network.cookie.cookieBehavior", 2)

browser = webdriver.Firefox(firefox_profile=fp)
browser.get("https://pl.pons.com/t%C5%82umaczenie?q=&l=frpl&in=&lf=fr&qnac=")

browser.implicitly_wait(15)
# cookie_button = browser.find_element_by_class_name("qc-cmp-button").click()
browser.implicitly_wait(15)
# button3 = browser.find_elements_by_xpath("//*[contains(text(), 'OK')]").click()
browser.quit()

button2 = browser.find_element_by_class_name(
    "qc-cmp-button qc-cmp-save-and-exit"
).click()


browser.find_elements_by_partial_link_text("ok").click()
cookie_button_close = browser.find_element_by_class_name(
    "qc-cmp-button qc-cmp-save-and-exit"
).click()



cookie_button = browser.find_element_by_css_selector(
    a"[onlick='window.__cmpui(&quot;setAndSaveAllConsent&quot;,!0)'"
).click()
"""
