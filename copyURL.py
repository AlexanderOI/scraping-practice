import pyautogui as pg
import pyperclip

pg.click(247, 60)
pg.hotkey('ctrl', 'c')

text_paste = pyperclip.paste()

with open("data/URL_products.txt", "a", encoding="utf-8") as file:
    file.write(text_paste + "\n")

print(text_paste)
