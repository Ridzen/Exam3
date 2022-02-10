# ______________________________________________________2_________________________________________
# Создайте класс Lemonade (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте проперти метод drink_info(), выводящий на печать «Газировка и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».

class Lemonade:

    def __init__(self, additives):
        if isinstance(additives, str):
            self._additives = additives
        else:
            self._additives = None

    @property
    def drink_info(self):
        if self._additives:
            return f'Лимонад с {self._additives}'
        else:
            return 'Обычная газировка'


lemonade = Lemonade('клубникой')
print(lemonade.drink_info)

