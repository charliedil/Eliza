#  Hi! This is my ELIZA program. Work in progress for sure.
import random
import re

subj = ""
obj = ""
name = input("[ELIZA]: Hi! My name is ELIZA. It's nice to meet you. What should I call you?\n")
test1outputs = ["Why are you", "Is there a reason why you are", "What do you mean when you say you are"]
test2outputs = ["Tell me more about your", "Your"]
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
    test1 = re.search("^I\sAM(.*)", usrinput.upper())
    test2 = re.search("\s*MY\s(.*)", usrinput.upper())
    if(test1):
        predicate = test1.group(1)
        usrinput=input(f"[ELIZA]: {test1outputs[random.randint(0,2)]}{predicate.lower()}\n[{name}]: ")
    elif(test2):
        ra = random.randint(0,2)
        if ra == 2:
            usrinput=input(f"[ELIZA]: How do/does your {test2.group(1).lower()} make you feel?")
        else:
            usrinput=input(f"[ELIZA]: {test2outputs[ra]} {test2.group(1).lower()}\n[{name}]: ")
    else:
        usrinput=input(f"[ELIZA]: I see.\n[{name}]: ")
print("Goodbye!")
