##In IDLE, Alt-3 commnets out a line
##ok
import pyautogui,time
#to minimize both shell and the current python file
for i in range(0,2):
 pyautogui.hotkey('alt','space')
 pyautogui.press('n')
#to get the chrome settings panel opened by clicking the three dots in the right hand top corner
 
pyautogui.click(1345,51) 
pyautogui.moveTo(1315,417,duration=0.25)
pyautogui.moveTo(959,417,duration=1.20)
pyautogui.press('enter')
#to open the chrome version in the window
time.sleep(2)
pyautogui.screenshot('C:\images\chromeVersion.png',region=(338,129, 1027, 412))
time.sleep(1)
# to minimize chrome window
pyautogui.hotkey('alt','space')
pyautogui.press('n')
#to create new email window
pyautogui.click(22,83)
#to fill in the recipient section
pyautogui.typewrite('email recipient')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
#to fill the subject line
pyautogui.typewrite('New Client Released')
pyautogui.press('tab')

time.sleep(2)
pyautogui.typewrite('Hi All,\n\n')
#insert section
pyautogui.click(177,63)
#image section
pyautogui.click(356,87)
#select an image
pyautogui.typewrite('C:\images\chromeVersion.png')
pyautogui.press('enter')
time.sleep(2)
#reach the end of the screenshot added
pyautogui.press('pagedown')
pyautogui.press('enter')
pyautogui.press('enter')

pyautogui.typewrite('This is the current version of chrome\n\nThanks,\nShivi.')
time.sleep(2)
#pyautogui.hotkey('ctrl','enter')
