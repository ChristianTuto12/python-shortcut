import pyautogui
class capture():
	def __init__(self):
		myScreenshot = pyautogui.screenshot()
		myScreenshot.save(f'capture.png')

