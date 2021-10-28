
import pyautogui as pt
from time import sleep
import pyperclip
import random
sleep(3)

position1 = pt.locateOnScreen("smiley.png", confidence=.6)
x = position1[0]
y = position1[1]


def get_message():
    global x,y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x + 70, y - 40, duration = .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)

    return whatsapp_message


def post_response(message):
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


def process_response(message):
    random_no = random.randrange(3)

    if "Happy Birthday "in str(message).lower():
        return "Thank you so much dear !"

    else:
        if "Belated Happy birthday wishes "in str(message).lower():
            return "Thank you so much"
        elif "Sorry for the late wishes"in str(message).lower():
            return "It's okay dear "
        elif "Have a great year ahead" in str(message).lower():
            return"Thank you and you too "

        else :
            return "Thank you for your wishes ."



def check_for_new_messages():
    pt.moveTo(x + 50, y - 45, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("circle.png", confidence = .7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                processed_message = process_response(get_message())
                post_response(processed_message)
                sleep(10)

            else:
                print("No messages")
                sleep(10)

        except(Exception):
            print("No new messages")





check_for_new_messages()

