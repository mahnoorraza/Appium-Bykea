import base64
import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction


desired_cap = {

  "platformName": "Android",
  "deviceName": "Android",
  "app": "C:\\Users\\HP\\Downloads\\apk\\Bykea Bike Taxi Delivery Payments_v5.38_apkpure.com.apk"
}
driver =webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


#    Test(unittest.TestCase):
def testName():
    time.sleep(10)
    touch = TouchAction(driver)
    TouchAction(driver).press(x=350, y=1000).move_to(x=350, y=300).release().perform()
    time.sleep(10)
    #bakery
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[8]/android.view.View[1]/android.widget.Image").click()
    time.sleep(7)
    #eggs
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.widget.Button").click()
    time.sleep(7)
    #quantity
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View").click()
    time.sleep(7)
    #select egg
    #driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View").click()
    #time.sleep(7)
    #like
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.widget.Button[1]").click()
    time.sleep(7)
    #quantity
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.widget.Button[3]").click()
    time.sleep(6)
    #basket
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.widget.Button").click()
    time.sleep(7)
    #click order summary
    driver.find_element_by_xpath("//android.view.View[@content-desc='Order Summary']/android.widget.TextView").click()

    ts = time.strftime("%Y_%m_%d_%H%M%S")
    activityname = driver.current_activity
    filename = activityname+ts
    time.sleep(10)
    driver.save_screenshot("C:/Users/HP/PycharmProjects/AppiumSandbox/Screenshots/"+filename+".png")

video_rawdata = driver.stop_recording_screen()
vide_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

filepath = os.path.join("C:/Users/HP/PycharmProjects/AppiumSandbox/Screenshots/", vide_name+".mp4")

with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))

#calling function
if __name__ == "__main__":
    driver.implicitly_wait(15)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView").click()
    time.sleep(2)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView[2]").click()
    time.sleep(2)
    driver.find_element_by_id("com.bykea.pk:id/phoneNumberEt").send_keys("03333777526")
    time.sleep(3)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView").click()
    time.sleep(17)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ImageView").click()
    testName()


