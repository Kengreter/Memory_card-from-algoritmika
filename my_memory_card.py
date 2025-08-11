from PyQt5.QtCore import Qt
from random import shuffle,randint
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget,
    QLabel, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QGroupBox,
    QRadioButton,
    QButtonGroup
)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

bossLine = QVBoxLayout()
question = QLabel('Какой национальности не существует?')
box = QGroupBox('Варианты ответов:')
boxbossline = QHBoxLayout()
boxline1 = QVBoxLayout()
boxline2 = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
radiogroup = QButtonGroup()
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Смурфы')
ans3 = QRadioButton('Чулымцы')
ans4 = QRadioButton('Алеуты')
radiogroup.addButton(ans1)
radiogroup.addButton(ans2)
radiogroup.addButton(ans3)
radiogroup.addButton(ans4)
button = QPushButton('Ответить')

ansbox = QGroupBox('Результат теста:')
maybeAnsbox = QLabel('Правильно или Неправильно')
rightAnsbox = QLabel('Правильный ответ')

lineAnsbox = QVBoxLayout()
lineAnsbox.addWidget(maybeAnsbox)
lineAnsbox.addWidget(rightAnsbox,alignment = Qt.AlignCenter)
ansbox.setLayout(lineAnsbox)
class Question:
    def __init__(self,question,rightans,wrong1,wrong2,wrong3):
        self.right = rightans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.question = question
    

boxline1.addWidget(ans1,alignment = Qt.AlignCenter)
boxline1.addWidget(ans2,alignment = Qt.AlignCenter)
boxline2.addWidget(ans3,alignment = Qt.AlignCenter)
boxline2.addWidget(ans4,alignment = Qt.AlignCenter)
boxbossline.addLayout(boxline1)
boxbossline.addLayout(boxline2)
box.setLayout(boxbossline)

line1.addWidget(question,alignment = Qt.AlignCenter)
line2.addWidget(button,alignment = Qt.AlignCenter)

ansbox.hide()
main_win.total = 0
main_win.score = 0

def show_result():
    box.hide()
    ansbox.show()
    button.setText('Следующий вопрос')

def show_question():
    ansbox.hide()
    box.show()
    button.setText('Ответить')
    radiogroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    radiogroup.setExclusive(True)

answers = [ans1,ans2,ans3,ans4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    rightAnsbox.setText(q.right)
    show_question()

def show_correct(res):
    maybeAnsbox.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        show_correct('Правильно! ;)')
        print('Статистика\nВсего вопросов:',main_win.total,'\nПравильных ответов:',main_win.score)
        print('Рейтинг:',(round(main_win.score/main_win.total*100,2)),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно! :(')
            print('Рейтинг:',(round(main_win.score/main_win.total*100,2)),'%')

def next_question():
    if len(question_list) == 0:
        message = f'Тест завершён!\
            \nРезультат теста:\
            \nВсего вопросов: {main_win.total}\
            \nПравильный ответов: {main_win.score}\
            \nРейтинг: {round(main_win.score/main_win.total*100,2)}%'
        question.setText(message)
        # radiogroup.hide()
        ansbox.hide()
        button.hide()
        return
    main_win.total += 1
    print('Статистика\nВсего вопросов:',main_win.total,'\nПравильных ответов:',main_win.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list.pop(cur_question)
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()



question_list = []
question_list.append(Question('Какой национальности не существует?','Смурфы','Алеуты','Чулымцы','Энцы'))
question_list.append(Question('Сколько букв в русском алфавите?','33','32','34','31'))
question_list.append(Question('Столица Греции?','Афины','Волос','Родос','Ираклион'))
question_list.append(Question('В каком году был основан клуб ФК Спартак?','1922','1923','1921','1924'))
question_list.append(Question('Дата рекорда Овечкина (895 шайб)?','6 Апреля 2025','5 Апреля 2025','3 Августа 2024','21 Октября 2024'))
question_list.append(Question('Какая максимальная скорость гепарда?',"130км/ч","120км/ч","110км/ч","100км/ч"))
question_list.append(Question('Где находится статуя <Родина мать зовёт>?',"Волгоград","Москва","Ленинград","Нижний Новгород"))
question_list.append(Question('В каком году ФК Спартак получил свой первую звезду над эмблемой?',"2002","2001","1999","2003"))
question_list.append(Question('В каком году я родился?',"2012","2011","2013","2010"))
question_list.append(Question('Столица Бразилии?',"Бразилиа","Рио-де-жанейро","Сан-палау","Сальвадор"))
question_list.append(Question('В каком году Рио-де-жанейро перестала быть столицей Бразилии?',"1960","1961","2003","2001"))
question_list.append(Question('Кто выиграл сезон премьер-лиги 2023/24?',"ФК Зенит","ФК ЦСКА","ФК Спартак","ФК Динамо"))
question_list.append(Question('У кого больше всего золотых мячей?',"Лионель Месси","Кристиано Рональдо","Рональдиньо","Лука Модрич"))
button.clicked.connect(click_OK)




bossLine.addLayout(line1)
bossLine.addWidget(box)
bossLine.addWidget(ansbox)
bossLine.addLayout(line2)
main_win.setLayout(bossLine)





next_question()
main_win.resize(400,400)
main_win.show()
app.exec_()
