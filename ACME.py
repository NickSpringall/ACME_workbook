
skills_score_list = {
    "python":"1",
    "ruby":"2",
    "bash":"4",
    "git":"8",
    "html":"16",
    "tdd":"32",
    "javascript":"128"
}

user_skills_score = (0)
user_skills_list = []
more_skills_check = ""
user_input = ""

while more_skills_check != "no":
    user_input = input("input a language you know: ")
    if user_input in skills_score_list:
        if user_input in user_skills_list:
            more_skills_check = input(f"You've already entered " + user_input + " as a skill, do you know any other languages? yes or no")
            continue
        user_skills_list.append(user_input)
        user_skills_score = int(user_skills_score) + int(skills_score_list[user_input])
        more_skills_check = input("Great! do you have another language? Yes or No? ")
    else:
        more_skills_check = input("sorry, that's not on the skills list do you know another language? Yes or No? ")

user_input = str(user_input)
print("Your score skills score is " + str(user_skills_score) + "!")


for skill in skills_score_list:
    if skill not in user_skills_list:
        print(f"you could increase your score to " + str(int(user_skills_score) + int(skills_score_list[skill])) + " if you learn " + skill)
