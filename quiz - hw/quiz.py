import pgzrun

WIDTH = 870
HEIGHT = 650 
TITLE = "space quiz!"
score = 0
time_left = 10
question_file_name = "quiz.txt"
is_game_over = False

#boxes
marquee_box = Rect(0,0, 880, 80)
question_box = Rect(0, 0, 650,150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

#numbers, lists, other variables
marquee_message = ""
ansboxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions_asked = []
question_count = 0
question_index_number = 0
question = []
#positioning of the boxes
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,  100)
answer_box1.move_ip(30, 270)
answer_box2.move_ip(380, 270)
answer_box3.move_ip(30,450)
answer_box4.move_ip(380, 450)
skip_box.move_ip(700, 270)

#functions (draw, reading, next_question, move_marquee, on_mouse_down, read_file)
def draw():
    #drawing the boxes and giving color
    global marquee_box
    screen.clear()
    screen.fill("pink")
    screen.draw.filled_rect(marquee_box, "white")
    screen.draw.filled_rect(question_box, "white")
    screen.draw.filled_rect(timer_box, "white")
    screen.draw.filled_rect(skip_box, "white")

    #coloring the answer boxes using a for loop
    for ansbox in ansboxes:
        screen.draw.filled_rect(ansbox, "white")

    #marquee message and using the textbox function

    marquee_message = f"Welcome! You are onn question {question_index_number} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box color = "pink")

    screen.draw.textbox(str(time_left), timer_box, color = "pink", shadow = (0.5, 0.5), scolor = "dim grey")

    screen.draw.textbox("skip question", skip_box, color = "pink")

    screen.draw.textbox(question[0].strip, question_box, color = "pink")

    index_number = 1
    for ansbox in ansboxes:
        screen.draw.textbox(question[index_number].strip(), ansbox, color = "white")

def update():
    move_marquee()

def reading():
    #reading out the questions
    global question_count, questions_asked
    q_text = open(question_file_name, "r")
    for row in q_text:
        questions_asked.append(row)
        question_count += 1
    q_text.close()

def next_question():
    #reading the right question
    global question_index_number
    question_index_number += 1
    return questions_asked.pop(0).split(",")

def move_marquee():
    marquee_box.x -= 1
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def on_mouse_down(pos):
    index_number = 1
    for ansbox in ansboxes:
        if ansbox.collidepoint(pos):
            if index_number is int(question[5]):
                right_answer()
            else:
                game_over()
        index_number += 1
    if skip.box.collidepoint(pos):
        skip_question()

reading()
question = reading()

pgzrun.go()