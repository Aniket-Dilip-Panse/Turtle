import pyautogui as pg
def shutdown():
    pg.hotkey('win')
    pg.write('cmd')
    pg.press('enter')
    pg.sleep(3)
    location=pg.position()
    pg.write('shutdown /s')
    pg.press('enter')
    pg.sleep(6)
    pg.press('enter')
shutdown()
