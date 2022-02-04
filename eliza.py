"""
ELIZA - The Charlie edition
The problem we seek to solve is to create an AI system that utilizes RegEx's (pattern matching) to ask questions and
engage with the user by identifying key phrases and restructuring the user's sentence based on that.

USAGE
When you first run the ELIZA script, you will first be prompted for your name. After this you will be prompted for your
pronouns. Your name will be used only in a few responses. Pronouns are not used at all as of now, ideally this will be
implemented in the future somehow. Once you have provided these responses, feel free to interact with ELIZA as you see
fit. ELIZA prefers DBT over CBT, so if she detects judgement statements, she will ask you to rephrase. When you are
finished with ELIZA, enter "exit".

EXAMPLE
[ELIZA]: Hi! My name is ELIZA. It's nice to meet you. What should I call you?
Charlie
[ELIZA]: It is very nice to meet you Charlie! I am looking forward to getting to know you
Please specify your pronouns in the format: subject/object.
For example, my pronouns are ze/zir. Other examples of pronoun sets are he/him, she/her, and they/them.
[Charlie]: he/him
[ELIZA]: Thank you, Charlie. How can I help you today? Note- when you are ready to end our
conversation, please type and enter "exit" by itself.
[Charlie]: I am ugly
[ELIZA]: That was a judgement statement. Can you rephrase that sentence without judgement?
[Charlie]: I am sorry
[ELIZA]: That's what I'm here for, Charlie.
[Charlie]: I am not happy with how I look
[ELIZA]: You are not happy with how you look
...
[Charlie]: exit
[ELIZA]: Goodbye!

ALGORITHM
The algorithm I implemented is rather basic. First, personal nouns like "I", "me", and "you" are substituted with the
opposite form. That is to say, "I" is replaced with "you", "you" is replaced with "me", etc. Once this substitution is
made, a series of pattern tests are run to detect different sentence structures or keywords. Depending on which pattern
test passes first, a response will be sent. For some patterns, like a sentence that begins with "YOU AM" (this is after
substitution, so the original sentence starts with "I AM") there are multiple possible responses that are picked by
picking a random integer. Some pattern or keyword matches have just one possible response. For example. I have coded
the keyword "suicidal" such that when this keyword occurs ELIZA automatically provides the suicide helpline number.
If no tests pass and there is a personal noun in the sentence, ELIZA will simply output the sentence after the
inital transformation. Example: Do you hate me -> Do I hate you?. If there are no personal nouns, then ELIZA will
use one of the default, context-free answers.
These checks are all coded in a while loop that terminates upon when the user inputs "exit".

VERSION
Python 3.10.0
"""
import random
import re

subj = ""
obj = ""
name = input("[ELIZA]: Hi! My name is ELIZA. It's nice to meet you. What should I call you?\n")
being_test_present_answers = ["You are", "Why are you", "What makes you", "Do you know why you are", "Can you tell me more about why you are"]
being_test_past_answers = ["You were", "Are you still", "Why were you"]
being_test_future_answers = ["Why do you think you will", "You will", "When will you"]
rev_being_test_present_answers = ["You think I am", "What makes you think I am"]
rev_being_test_past_answers = ["You think I was", "How do you know I was", "What makes you think I was"]
rev_being_test_future_answers = ["You think I will", "What makes you think I will", "How do you know I will"]
pronouns_test_answers = ["Why do you think", "What makes you think", "How do you know"]

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
    sentfrags = []
    if(re.search(r"\bI\b", original)):
        usrinput = re.sub(r"\bI\b", "YOU", usrinput)
    if(re.search(r"(\bMYSELF\b)",original)):
        usrinput = re.sub(r"(\bMYSELF\b)", "YOURSELF", usrinput)
    if(re.search(r"(\bME\b)",original)):
        usrinput = re.sub(r"(\bME\b)", "YOU", usrinput)
    if(re.search(r"(\bMY\b)",original)):
        usrinput = re.sub(r"(\bMY\b)", "YOUR", usrinput)
    if(re.search(r"\bYOURSELF\b", original)):
        usrinput = re.sub(r"(\bYOURSELF\b)", "MYSELF", usrinput)
    if(re.search(r"\bYOU\b", original)):
        usrinput = re.sub(r"(\bYOU\b)", "I", usrinput)
    if(re.search(r"\bYOUR\b", original)):
        usrinput = re.sub(r"(\bYOUR\b)", "MY", usrinput)



    # print(usrinput)
    being_test_present = re.search(r"^YOU\sAM(.*)", usrinput)
    being_test_past = re.search(r"^YOU\sWAS(.*)", usrinput)
    being_test_future = re.search(r"^YOU\sWILL(.*)", usrinput)
    rev_being_test_present = re.search(r"^I\sARE(.*)", usrinput)
    rev_being_test_past = re.search(r"^I\sWERE(.*)", usrinput)
    rev_being_test_future = re.search(r"^I\sWILL(.*)", usrinput)
    absolute_test = re.search(r"(\bALWAYS\b|\bNEVER\b|\bNOBODY\b|\bEVERYBODY\b|\bEVERYONE\b|\bANYONE\b|\bANYBODY\b)", usrinput)
    hate_or_love_test = re.search(r"\bHATES*\b|\bLOVES*\b", usrinput)
    suicidality_test = re.search(r"\bSUICIDAL\b", usrinput)
    thanks_sorry_test = re.search(r"\bSORRY\b|\bTHANK\b|\bTHANKS\b", usrinput)
    pronouns_test = re.search(r"(^SHE|^HE|^THEY|^ZE)(.*)", usrinput)
    want_need_test = re.search(r"(^YOU WANT|^YOU NEED|^YOU CRAVE)(.*)", usrinput)
    family_test = re.search(r"(\bFATHER\b|\bMOTHER\b|\bDAD\b|\bMOM\b|\bBROTHER\b|\bSIBLING\b|\bSISTER\b|\bGRANDMA\b|\bGRANDMOTHER\b|\bGRANDFATHER\b|\bGRANDPA\b|\bAUNT\b|\bUNCLE\b|\bHUSBAND\b|\bWIFE\b|\bSPOUSE\b|\bPARENT\b)", usrinput)
    judgement_words = re.search(r"\bSTUPID\b|\bUGLY\b|\bANNOYING\b", usrinput)
    fail_safe = re.search(r"\bI\b|\bYOU\b|\bME\b|\bMYSELF\b|\bMY\b|\bYOUR\b|\bYOURSELF\b", usrinput)
    if(suicidality_test):
        usrinput = input(f"[ELIZA]: It seems like you may be feeling some strong emotions right now. You are very brave for being honest with me. \nHere is a number for you to call that may be more help than I can be: 800-273-8255.\n[{name}]: ")
    elif(want_need_test):
        usrinput = input(f"[ELIZA]: Where do you think this desire to have{want_need_test.group(2).lower()} stems from?\n[{name}]: ")
    elif(family_test):
        usrinput = input(f"[ELIZA]: Can you tell me more about your {family_test.group(1).lower()}\n[{name}]: ")
    elif(judgement_words):
        usrinput = input(f"[ELIZA]: That was a judgement statement. Can you rephrase that sentence without judgement?\n[{name}]: ")
    elif(thanks_sorry_test):
        usrinput = input(f"[ELIZA]: That's what I'm here for, {name}.\n[{name}]: ")
    elif(absolute_test):
        usrinput = input(f"[ELIZA]: {absolute_test.group(1).lower().capitalize()}?\n[{name}]: ")
    elif(hate_or_love_test):
        usrinput = input(f"[ELIZA]: Why do you say the word {hate_or_love_test.group(0).lower()}? What made you choose this word as opposed to a different one?\n[{name}]: ")
    elif(being_test_present):
        usrinput = input(f"[ELIZA]: {being_test_present_answers[random.randint(0,len(being_test_present_answers)-1)]}{being_test_present.group(1).lower()}\n[{name}]: ")
    elif(being_test_past):
        usrinput = input(f"[ELIZA]: {being_test_past_answers[random.randint(0,len(rev_being_test_past_answers)-1)]}{being_test_past.group(1).lower()}\n[{name}]: ")
    elif(being_test_future):
        usrinput = input(f"[ELIZA]: {being_test_future_answers[random.randint(0, len(rev_being_test_future_answers)-1)]}{being_test_future.group(1).lower()}\n[{name}]: ")
    elif(rev_being_test_present):
        usrinput = input(f"[ELIZA]: {rev_being_test_present_answers[random.randint(0,len(rev_being_test_present_answers)-1)]}{rev_being_test_present.group(1).lower()}\n[{name}]: ")
    elif(rev_being_test_past):
        usrinput = input(f"[ELIZA]: {rev_being_test_past_answers[random.randint(0,len(rev_being_test_past_answers)-1)]}{rev_being_test_past.group(1).lower()}\n[{name}]: ")
    elif(rev_being_test_future):
        usrinput = input(f"[ELIZA]: {rev_being_test_future_answers[random.randint(0, len(rev_being_test_future_answers)-1)]}{rev_being_test_future.group(1).lower()}\n[{name}]: ")
    elif(pronouns_test):
        usrinput = input(f"[ELIZA]: {pronouns_test_answers[random.randint(0,len(pronouns_test_answers)-1)]} {pronouns_test.group(1).lower()}{pronouns_test.group(2).lower()}?\n[{name}]: ")
    elif(fail_safe):
        usrinput = input(f"[ELIZA]: {usrinput.lower()}\n[{name}]: ")
    else:
        usrinput=input(f"[ELIZA]: {defaultanswers[random.randint(0,len(defaultanswers)-1)]}\n[{name}]: ")
print("[ELIZA]: Goodbye!")