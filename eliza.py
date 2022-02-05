"""
ELIZA
Charlie Dil
02/05/2022

PROBLEM STATEMENT
The problem we seek to solve is to create an AI system that utilizes RegEx's (pattern matching) to ask questions and
engage with the user by identifying key phrases and restructuring the user's sentence based on that.

USAGE
When you first run the ELIZA script, you will first be prompted for your name. After this you will be prompted for your
pronouns. Your name will be used only in a few responses. Pronouns are not used at all as of now, ideally this will be
implemented in the future somehow. Once you have provided these responses, feel free to interact with ELIZA as you see
fit. ELIZA prefers DBT over CBT, so if she detects judgement statements, she will ask you to rephrase. When you are
finished with ELIZA, enter "exit".
NOTE: ELIZA expects basic SVO sentences, and one at a time.

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
opposite form. That is to say, "I" is replaced with "you", "you" is replaced with "I", etc. Once this substitution is
made, a series of pattern tests are run to detect different sentence structures or keywords. Depending on which pattern
test passes first, a response will be sent. For some patterns, like a sentence that begins with "YOU AM" (this is after
substitution, so the original sentence starts with "I AM") there are multiple possible responses that are picked by
picking a random integer. Some pattern or keyword matches have just one possible response. For example. I have coded
the keyword "suicidal" such that when this keyword occurs ELIZA automatically provides the suicide helpline number.
If no tests pass and there is a personal noun in the sentence, ELIZA will simply output the sentence after the
inital transformation. Example: Do you like me -> Do I like you?. If there are no personal nouns, then ELIZA will
use one of the default, context-free answers, such as "I see".
These checks are all coded in a while loop that terminates upon when the user inputs "exit".

VERSION
Python 3.10.0
"""
import random
import re

# These variables are used to store the user's pronouns, e.g. for me subj==he and obj==him
subj = ""
obj = ""

# These are the pool of responses for each test. So if the beting_test_present passes, a string from the corresponding
# array is chosen. Same for the rest of the tests.
being_test_present_answers = ["You are", "Why are you", "What makes you", "Do you know why you are", "Can you tell me more about why you are"]
being_test_past_answers = ["You were", "Are you still", "Why were you"]
being_test_future_answers = ["Why do you think you will", "You will", "When will you"]
rev_being_test_present_answers = ["You think I am", "What makes you think I am"]
rev_being_test_past_answers = ["You think I was", "How do you know I was", "What makes you think I was"]
rev_being_test_future_answers = ["You think I will", "What makes you think I will", "How do you know I will"]
pronouns_test_answers = ["Why do you think", "What makes you think", "How do you know"]

# If no test including the fail-safe test passes, one of these answers is randomly picked.
defaultanswers = ["I see", "What else is on your mind?", "I don't really understand"]


# Prompt user for name and store in name var
name = input("[ELIZA]: Hi! My name is ELIZA. It's nice to meet you. What should I call you?\n")

# Prompt user for pronouns, store raw input in pronouns
pronouns = input(f"[ELIZA]: It is very nice to meet you {name}! I am looking forward to getting to know you\n"
            f"Please specify your pronouns in the format: subject/object. \nFor example, "
            f"my pronouns are ze/zir. Other examples of pronoun sets are he/him, she/her, and they/them.\n[{name}]:")

# Ensure that raw input is in expected format, if not, keep asking.
while len(pronouns.split("/"))<2:
    pronouns = input(f"[ELIZA]: Please provide pronouns in the requested format. subject/object\n[{name}]: ")

# Once we have ensured valid input, we save them in the vars defined above
subj = pronouns.split("/")[0].upper() # e.g. subj==he
obj = pronouns.split("/")[1].upper() # e.g. obj==him

# Getting the first actual input from user and storing it.
usrinput = input(f"[ELIZA]: Thank you, {name}. How can I help you today? Note- when you are ready to end our\nconversation,"
                 f" please type and enter \"exit\" by itself.\n[{name}]: ")

# We want to keep engaging with the user until the user sends "exit" or "EXIT", hence WHILE
while usrinput.upper()!="EXIT":
    # Convert input to uppercase to mitigate input inconsistencies
    original = usrinput.upper()
    # No punctuation, we assume single and simple sentences as input
    usrinput = re.sub("[\.\,\?\!]","", original)
    # For the substitutions of personal nouns, we break the sentence back into words stored in sentfrags
    sentfrags = []
    # This dictionary maps each personal noun into what it should be transformed into
    personalNouns = {"I":"YOU", "MYSELF":"YOURSELF","ME":"YOU","MY":"YOUR","YOURSELF":"MYSELF","YOU":"I", "YOUR":"MY"}
    # initialization of sentfrags
    sentfrags = usrinput.split(" ")

    # we check each word in sentfrags - if it is in the personalNouns dict, we replace it with its associated noun
    for s in range(len(sentfrags)):
        if sentfrags[s] in personalNouns:
            sentfrags[s] = personalNouns[sentfrags[s]]
    # now we append the words with spaces back into the usrinput var
    usrinput = ""
    for s in sentfrags:
        usrinput+= s
        usrinput+=" "

    # These are all of the regex tests ran on the input. We use the results to determine what output to print.
    # First set of tests are looking for sentence using the verb to be
    being_test_present = re.search(r"^YOU\sAM(.*)", usrinput)
    being_test_past = re.search(r"^YOU\sWAS(.*)", usrinput)
    being_test_future = re.search(r"^YOU\sWILL(.*)", usrinput)
    rev_being_test_present = re.search(r"^I\sARE(.*)", usrinput)
    rev_being_test_past = re.search(r"^I\sWERE(.*)", usrinput)
    rev_being_test_future = re.search(r"^I\sWILL(.*)", usrinput)

    # This test is looking for absolute adjectives
    absolute_test = re.search(r"(\bALWAYS\b|\bNEVER\b|\bNOBODY\b|\bEVERYBODY\b|\bEVERYONE\b|\bANYONE\b|\bANYBODY\b)", usrinput)
    # This test is looking for strong words, specifically hates and loves
    hate_or_love_test = re.search(r"\bHATES*\b|\bLOVES*\b", usrinput)
    # This test is testing for suicidality
    suicidality_test = re.search(r"\bSUICIDAL\b", usrinput)
    # testing for apologies or thank you's
    thanks_sorry_test = re.search(r"\bSORRY\b|\bTHANK\b|\bTHANKS\b", usrinput)
    # testing for pronouns
    pronouns_test = re.search(r"(^SHE|^HE|^THEY|^ZE)(.*)", usrinput)
    # testing for desires
    want_need_test = re.search(r"(^YOU WANT|^YOU NEED|^YOU CRAVE)(.*)", usrinput)
    # testing for mentions of family
    family_test = re.search(r"(\bFATHER\b|\bMOTHER\b|\bDAD\b|\bMOM\b|\bBROTHER\b|\bSIBLING\b|\bSISTER\b|\bGRANDMA\b|\bGRANDMOTHER\b|\bGRANDFATHER\b|\bGRANDPA\b|\bAUNT\b|\bUNCLE\b|\bHUSBAND\b|\bWIFE\b|\bSPOUSE\b|\bPARENT\b)", usrinput)
    # DBT test
    judgement_words = re.search(r"\bSTUPID\b|\bUGLY\b|\bANNOYING\b", usrinput)
    # If no patterns are matched and a personal noun is used, then we should just output the modified sentence
    # as a sort of fail safe. Still better than a context free answer.
    fail_safe = re.search(r"\bI\b|\bYOU\b|\bME\b|\bMYSELF\b|\bMY\b|\bYOUR\b|\bYOURSELF\b", usrinput)

    # We check to see which tests past and specify what we want to output here. Only one branch will execute
    # The ordering is based off of priority. Some tests only have one answer, some have a set detailed above
    # that must be chosen from randomly.
    if(suicidality_test):
        # static response: provide suicide hotline
        usrinput = input(f"[ELIZA]: It seems like you may be feeling some strong emotions right now. You are very brave for being honest with me. \nHere is a number for you to call that may be more help than I can be: 800-273-8255.\n[{name}]: ")
    elif(want_need_test):
        # transform sentence using the desire in question
        usrinput = input(f"[ELIZA]: Where do you think this desire to have{want_need_test.group(2).lower()} stems from?\n[{name}]: ")
    elif(family_test):
        # transform sentence using family member
        usrinput = input(f"[ELIZA]: Can you tell me more about your {family_test.group(1).lower()}\n[{name}]: ")
    elif(judgement_words):
        # static response: DBT encourages to avoid judgement statements
        usrinput = input(f"[ELIZA]: That was a judgement statement. Can you rephrase that sentence without judgement?\n[{name}]: ")
    elif(thanks_sorry_test):
        # response that uses name provided in the beginning
        usrinput = input(f"[ELIZA]: That's what I'm here for, {name}.\n[{name}]: ")
    elif(absolute_test):
        # response that uses absolute adverb as question
        usrinput = input(f"[ELIZA]: {absolute_test.group(1).lower().capitalize()}?\n[{name}]: ")
    elif(hate_or_love_test):
        # response that uses hate or love very provided in question
        usrinput = input(f"[ELIZA]: Why do you say the word {hate_or_love_test.group(0).lower()}? What made you choose this word as opposed to a different one?\n[{name}]: ")
    elif(being_test_present):
        # Output selected randomly combined with the object of the linking verb
        usrinput = input(f"[ELIZA]: {being_test_present_answers[random.randint(0,len(being_test_present_answers)-1)]}{being_test_present.group(1).lower()}\n[{name}]: ")
    elif(being_test_past):
        # Output selected randomly combined with the object of the linking verb
        usrinput = input(f"[ELIZA]: {being_test_past_answers[random.randint(0,len(rev_being_test_past_answers)-1)]}{being_test_past.group(1).lower()}\n[{name}]: ")
    elif(being_test_future):
        # Output selected randomly combined with the object of the linking verb
        usrinput = input(f"[ELIZA]: {being_test_future_answers[random.randint(0, len(rev_being_test_future_answers)-1)]}{being_test_future.group(1).lower()}\n[{name}]: ")
    elif(rev_being_test_present):
        # Output selected randomly combined with the object of the linking verb
        usrinput = input(f"[ELIZA]: {rev_being_test_present_answers[random.randint(0,len(rev_being_test_present_answers)-1)]}{rev_being_test_present.group(1).lower()}\n[{name}]: ")
    elif(rev_being_test_past):
        # Output selected randomly combined with the object of the linking verb
        usrinput = input(f"[ELIZA]: {rev_being_test_past_answers[random.randint(0,len(rev_being_test_past_answers)-1)]}{rev_being_test_past.group(1).lower()}\n[{name}]: ")
    elif(rev_being_test_future):
        # Output selected randomly combined with the object of the linking verb
        usrinput = input(f"[ELIZA]: {rev_being_test_future_answers[random.randint(0, len(rev_being_test_future_answers)-1)]}{rev_being_test_future.group(1).lower()}\n[{name}]: ")
    elif(pronouns_test):
        # Output selected randomly combined with the object of the sentence
        usrinput = input(f"[ELIZA]: {pronouns_test_answers[random.randint(0,len(pronouns_test_answers)-1)]} {pronouns_test.group(1).lower()}{pronouns_test.group(2).lower()}?\n[{name}]: ")
    elif(fail_safe):
        # Just returns the output sentence with replacements
        usrinput = input(f"[ELIZA]: {usrinput.lower()}\n[{name}]: ")
    else:
        # Randomly pick a default response
        usrinput=input(f"[ELIZA]: {defaultanswers[random.randint(0,len(defaultanswers)-1)]}\n[{name}]: ")

# Once we are out of the loop, that means the user has said "exit" so we can say goodbye now!
print("[ELIZA]: Goodbye!")