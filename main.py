import pyautogui
import pyperclip
import ai_api


# Move the mouse to the first icon location and click
pyautogui.click(1186 , 1046)

# Drag the cursor to the desired location
pyautogui.moveTo(735 , 217)
pyautogui.dragTo(1811 , 900, duration=1)

# Perform a copy action
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1567 , 570)
pyautogui.click(1186 , 1046)

# Save the copied content to a variable
copied_content = pyperclip.paste()

print(f"Copied content: {copied_content}")
a = ai_api.ai(copied_content)
print(a)

pyperclip.copy(a)
pyautogui.click(1186 , 1046)
pyautogui.moveTo(1227, 949)
pyautogui.click()

# Paste the text
pyautogui.hotkey('ctrl', 'v')

# Press the Enter key
pyautogui.press('enter')