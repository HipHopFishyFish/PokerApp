import cardsModule as cm
import gui, threading

table = gui.PokerTable()
cards = cm.makeCards()
a = threading.Thread(target = table.round, args=(cards, 1))
a.start()

table.mainloop()