#  Hi! This is my ELIZA program. Work in progress for sure.
import random
import re

subj = ""
obj = ""
name = input("[ELIZA]: Hi! My name is ELIZA. It's nice to meet you. What should I call you?\n")
being_test_present_answers = ["You are", "Why are you", "What makes you", "Do you know why you", "Can you tell me more about why you"]
being_test_past_answers = ["You were", "Are you still", "Why were you"]
being_test_future_answers = ["Why do you think you will", "You will", "When will you"]
rev_being_test_present_answers = ["You think I am", "What makes you think I am"]
rev_being_test_past_answers = ["You think I was", "How do you know I was", "What makes you think I was"]
rev_being_test_future_answers = ["You think I will", "What makes you think I will", "How do you know I will"]
defaultanswers = ["I see", "What else is on your mind?", "I don't really understand"]
pronouns = input(f"[ELIZA]: It is very nice to meet you {name}! I am looking forward to getting to know you\n"
            f"Please specify your pronouns in the format: subject/object. \nFor example, "
            f"my pronouns are ze/zir. Other examples of pronoun sets are he/him, she/her, and they/them.\n[{name}]:")
while len(pronouns.split("/"))<2:
    pronouns = input(f"[ELIZA]: Please provide pronouns in the requested format. subject/object\n[{name}]: ")

subj = pronouns.split("/")[0].upper()
obj = pronouns.split("/")[1].upper()
usrinput = input(f"[ELIZA]: Thank you, {name}. How can I help you today? Note- when you are ready to end our\nconversation,"
                 f" please type and enter \"exit\" by itself.\n[{name}]: ")
while usrinput.upper()!="EXIT":
    original = usrinput.upper()
    usrinput = re.sub("[\.\,\?\!]","", original)
    if(re.search("(^I\s)", original)):
        usrinput = re.sub("(^I\s)", "YOU ", usrinput)
    if(re.search("(\sI\s)", original)):
        usrinput = re.sub("(\sI\s)", " YOU ", usrinput)
    if(re.search("\sI$", original)):
        usrinput = re.sub("\sI$", " YOU", usrinput)
    if(re.search("(^MYSELF\s)",original)):
        usrinput = re.sub("(^MYSELF\s)", "YOURSELF ", usrinput)
    if(re.search("(\sMYSELF\s)",original)):
        usrinput = re.sub("(\sMYSELF\s)", " YOURSELF ", usrinput)
    if(re.search("\sMYSELF$",original)):
        usrinput = re.sub("\sMYSELF$", " YOURSELF", usrinput)
    if(re.search("(^ME\s)",original))
        usrinput = re.sub("(^ME\s)", "YOU ", usrinput)
    if(re.search("(\sME\s)",original)):
        usrinput = re.sub("(\sME\s)", " YOU ", usrinput)
    if(re.search("\sME$", original)):
        usrinput = re.sub("\sME$", " YOU", usrinput)
    if(re.search("(^MY\s)",original)):
        usrinput = re.sub("(^MY\s)", "YOUR ", usrinput)
    if(re.search("(\sMY\s)", original)):
        usrinput = re.sub("(\sMY\s)", " YOUR ", usrinput)
    usrinput = re.sub("\sMY$", " YOUR", usrinput)
    usrinput = re.sub("(^YOURSELF\s)", "MYSELF ", usrinput)
    usrinput = re.sub("(\sYOURSELF\s)", " MYSELF ", usrinput)
    usrinput = re.sub("\sYOURSELF$", " MYSELF", usrinput)
    usrinput = re.sub("(^YOU\s)", "I ", usrinput)
    usrinput = re.sub("(\sYOU\s)", " I ", usrinput)
    usrinput = re.sub("\sYOU$", " ME", usrinput)
    usrinput = re.sub("(^YOUR\s)", "MY ", usrinput)
    usrinput = re.sub("(\sYOUR\s)", " MY ", usrinput)
    usrinput = re.sub("\sYOUR$", " MY", usrinput)
    usrinput = re.sub("(^ARE\s)", "YOURSELF ", usrinput)
    usrinput = re.sub("(\sMYSELF\s)", " YOURSELF ", usrinput)
    usrinput = re.sub("\sMYSELF$", " YOURSELF", usrinput)

    print(usrinput)
    being_test_present = re.search("^YOU\sAM(.*)", usrinput)
    being_test_past = re.search("^YOU\sWAS(.*)", usrinput)
    being_test_future = re.search("^YOU\sWILL(.*)", usrinput)
    rev_being_test_present = re.search("^I\sARE(.*)", usrinput)
    rev_being_test_past = re.search("^I\sWERE(.*)", usrinput)
    rev_being_test_future = re.search("^I\sWILL(.*)", usrinput)
    if(being_test_present):
        usrinput = input(f"[ELIZA]: {being_test_present_answers[random.randint(0,len(being_test_present_answers)-1)]}{being_test_present.group(1)}\n[{name}]: ")

    else:
        usrinput=input(f"[ELIZA]: I see.\n[{name}]: ")
print("Goodbye!")
