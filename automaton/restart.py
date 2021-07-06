import pyautogui as pg
def restart():
    pg.hotkey('win')
    pg.write('cmd')
    pg.press('enter')
    pg.sleep(3)
    location=pg.position()
    pg.write('shutdown /r')
    pg.press('enter')
    pg.sleep(6)
    pg.press('enter')
restart()