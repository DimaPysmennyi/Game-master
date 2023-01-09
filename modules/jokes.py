import modules.npc as npc
jokes = [
    ["Нашій кішці спочатку не сподобався пилесос, а потім вона", "втягнулася."],
    ["— Вітаю, мене звати Сергій, і я брехун.", "— Сідайте, Сергій.", "— Я не Сергій."],
    ["У магазин «Все по 50» завезли долар."],
    ["Заходить чоловік в аптеку, питає:", "— Дайте медицинський спирт.", "— Є рецепт?", "— Був би, сам би зробив."],
    ["— Чому поганого шпіона називають Гігачадом?", "— Видає базу."]
]

def tell(joke_index, win):
    if joke_index == 0:
        npc.illya.show_text(jokes[joke_index][0], win, 35, 55, 675)
        npc.illya.show_text(jokes[joke_index][1], win, 35, 55, 705)

    if joke_index == 1:
        npc.illya.show_text(jokes[joke_index][0], win, 35, 55, 675)
        npc.illya.show_text(jokes[joke_index][1], win, 35, 55, 705)
        npc.illya.show_text(jokes[joke_index][2], win, 35, 55, 735)
        
    if joke_index == 2:
        npc.illya.show_text(jokes[joke_index][0], win, 35, 55, 675)

    if joke_index == 3:
        npc.illya.show_text(jokes[joke_index][0], win, 35, 55, 675)
        npc.illya.show_text(jokes[joke_index][1], win, 35, 55, 705)
        npc.illya.show_text(jokes[joke_index][2], win, 35, 55, 735)
        npc.illya.show_text(jokes[joke_index][3], win, 35, 55, 765)

    if joke_index == 4:
        npc.illya.show_text(jokes[joke_index][0], win, 35, 55, 675)
        npc.illya.show_text(jokes[joke_index][1], win, 35, 55, 705)