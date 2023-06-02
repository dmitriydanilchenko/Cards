
class Player:
    def __init__(self,name,age,sity):
        self.name = name
        self.age = age
        self.sity = sity
        print(f'Привествую {name}, в моей игре Cards vs Humans')
        print('Правила просты.\nВы загадываете карту,\nа компьютер пытается ее отгадать')
        print('Варианты выбора карт таковы - ', Cards.variants)

class Cards:
    variants = ('6','7','8','9','10','Валет', 'Дама', 'Король', 'Туз')
    def __init__(self,card):
        self.card = card
        while self.card not in Cards.variants:
            self.card = input('Такой карты не существует\nВыберите карту из списка ')
        print('Ваша карта загадана')
    @staticmethod
    def otgad():
        num=0
        for i in Cards.variants:
            num +=1
            otvet = input(f'Ваша карта {i} ')
            if  otvet == 'да':
                print(f'игра окончена\nпопыток {num}')
                break
            elif num == 9:
                print(f'Вы нам соврали, все варианты были пройдены')




print('Введите ваше имя возраст и город')
Player1 = Player(input('Имя '), input('Возраст '), input('Город '))
print('Теперь загадайте карту из списка')
Card1 = Cards(input('Вы загадываете карту - '))
Cards.otgad()