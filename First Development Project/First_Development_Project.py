print("Hi welcome to the quiz game. You will have 3 lives to finish and win this game")
questions = [
    "What does the term 'phishing' refer to in the context of E-Safety?\n"
    "a) A fraudulent attempt to obtain sensitive information\n"
    "b) A type of computer virus\n"
    "c) A form of online bullying",

    "Which of the following is NOT a good practice for creating strong and secure passwords?\n"
    "a) Using a combination of upper and lower case letters\n"
    "b) Using easily guessable information\n"
    "c) Incorporating special characters like !, @, or #",

    "What should you do if you receive an unsolicited email or message that asks for your personal information?\n"
    "a) Reply with your information to be helpful\n"
    "b) Share the message with your friends on social media\n"
    "c) Delete the message and do not respond",

    "Social media platforms often allow you to control the privacy settings of your account. What should you typically set your profile to in order to enhance E-Safety?\n"
    "a) Public, so everyone can see your posts\n"
    "b) Only visible to people from your school or workplace\n"
    "c) Private, so only approved friends or followers can see your contentOnly visible to people from your school or workplace",

    "Which of the following is an example of cyberbullying?\n"
    "a) A friendly joke shared among friends in a group chat\n"
    "b) Repeated, hurtful comments posted online with the intent to harm or harass someone\n"
    "c) An online quiz like this one",

    "When downloading software or apps, which source is generally the safest to use?\n"
    "a) Official app stores like Apple's App Store or Google Play\n"
    "b) Third-party websites with good reviews\n"
    "c) Random links shared by friends on social media",

    "You receive a message from someone online who claims to be a long-lost relative and asks for your address to send you a gift. What should you do?\n"
    "a) Share your address, since it's a relative\n"
    "b) Politely decline and do not share any personal information\n"
    "c) Ask for a picture of the gift first",
]

correct_answers = ['a', 'b', 'c', 'c', 'b', 'a', 'b']
play_again = True

while play_again:
    score = 0
    lives = 3

    for i, question in enumerate(questions):
        print(f"Question {i + 1} (Lives: {lives}):\n{question}")
        user_answer = input("Enter your answer (a/b/c): ").lower()

        if user_answer == correct_answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
            lives -= 1
            if lives == 0:
                print("Game over! You've run out of lives.")
                break

    print(f"Your final score is: {score}/{len(questions)}")
    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input != "yes":
        play_again = False
