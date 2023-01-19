import modules.npc as npc
jokes = [
    ["Нашій кішці спочатку не сподобався пилесос, а потім вона", "втягнулася.", 0],
    ["— Вітаю, мене звати Сергій, і я брехун.", "— Сідайте, Сергій.", "— Я не Сергій.", 0],
    ["У магазин «Все по 50» завезли долар.", 0],
    ["Заходить чоловік в аптеку, питає:", "— Дайте медицинський спирт.", "— Є рецепт?", "— Був би, сам би зробив.", 0],
    ["— Чому поганого шпіона називають Гігачадом?", "— Видає базу.", 0]
]

def tell(joke_index, win):
    if joke_index == 0:
        if npc.illya.CURRENT_STR >= 3:
            jokes[0][2] += 1
            npc.illya.show_text(jokes[joke_index][0][0:jokes[0][2]], win, 35, 55, 675)
            npc.illya.show_text(jokes[joke_index][1][0:jokes[0][2]], win, 35, 55, 705)

    if joke_index == 1:
        if npc.illya.CURRENT_STR >= 3:
            jokes[1][3] += 1
            npc.illya.show_text(jokes[joke_index][0][0:jokes[1][3]], win, 35, 55, 675)
            npc.illya.show_text(jokes[joke_index][1][0:jokes[1][3]], win, 35, 55, 705)
            npc.illya.show_text(jokes[joke_index][2][0:jokes[1][3]], win, 35, 55, 735)
        
    if joke_index == 2:
        if npc.illya.CURRENT_STR >= 3:
            jokes[2][1] += 1
            npc.illya.show_text(jokes[joke_index][0][0:jokes[2][1]], win, 35, 55, 675)

    if joke_index == 3:
        if npc.illya.CURRENT_STR >= 3:
            jokes[3][3] += 1
            npc.illya.show_text(jokes[joke_index][0][0:jokes[3][3]], win, 35, 55, 675)
            npc.illya.show_text(jokes[joke_index][1][0:jokes[3][3]], win, 35, 55, 705)
            npc.illya.show_text(jokes[joke_index][2][0:jokes[3][3]], win, 35, 55, 735)
            npc.illya.show_text(jokes[joke_index][3][0:jokes[3][3]], win, 35, 55, 765)

    if joke_index == 4:
        if npc.illya.CURRENT_STR >= 3:
            jokes[4][3] += 1
            npc.illya.show_text(jokes[joke_index][0][0:jokes[4][3]], win, 35, 55, 675)
            npc.illya.show_text(jokes[joke_index][1][0:jokes[4][3]], win, 35, 55, 705)