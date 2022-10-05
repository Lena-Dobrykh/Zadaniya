from random import randint
from f import was_asked, old_answer
memory = []
prompt = " Вопрос: "
answers = ("да","нет")
question=""
while question !="стоп":
    print(prompt, end = ' ')
    question = input()
    if was_asked(memory, question):
        print(old_answer())
    else:
        answer = answers[randint(0,len(answers)-1)]
        print(answer)
        memory += [ (question, answer) ]
