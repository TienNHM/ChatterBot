from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious", database = "db.sqlite3")

def Train():
    from chatterbot.trainers import ListTrainer

    conversation = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome.",
    ]

    trainer = ListTrainer(chatbot)

    trainer.train(conversation) 
    trainer.train(
        ["Xin chào!",
         "Chào bạn nha! Dạo này khỏe không?",
         "Oh tôi khỏe. Bạn thì sao?",
         "Ah mình cũng khỏe.",
         "Công việc của bạn dạo này tiến triển tốt chứ?",
         "Cũng khá tốt.",
         "Trễ giờ rồi, tạm biệt nha.",
         "Tạm biệt!"
         ])

def Demo():
    while True:
        input_text = input()
        if input_text=="":
            return

        response = chatbot.get_response(input_text)
        print(response)

if __name__=="__main__":
    print("", end="\n\n")
    re = input("(Train = 0, Demo = 1). Choose: ")
    if re=="0":
        Train()
    elif re=="1":
        Demo()
    print("--------------------------------------")