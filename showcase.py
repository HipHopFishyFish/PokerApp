import cardsModule as cm
import threading as thr
from gui import cards as guicards
import gui
import time


table = gui.PokerTable()
cards = cm.makeCards()
def showall():
    oldcard = table.canvas.create_text(250, 250, text="CARD SHOWCASE", font=("Ariel", 40))
    time.sleep(2)
    for card in cards.cards:
        mycard = cm.Card(card.number, card.suit)
        card = oldcard
        card = guicards.display_card(table, mycard, 200, 300)
        time.sleep(.07)
        table.canvas.delete(oldcard)
    time.sleep(1)
    table.canvas.delete(card)
    time.sleep(.5)
    table.master.quit()
thr.Thread(target=showall).start()

table.mainloop()