#  Hi! This is my ELIZA program. Work in progress for sure.
subj = ""
obj = ""
name = input("[ELIZA]: Hi! My name is ELIZA. It's nice to meet you. What should I call you?\n")

pronouns = input(f"[ELIZA]: It is very nice to meet you {name}! I am looking forward to getting to know you\n"
            f"Please specify your pronouns in the format: subject/object. \nFor example, "
            f"my pronouns are ze/zir. Other examples of pronoun sets are he/him, she/her, and they/them.\n[{name}]:")
while len(pronouns.split("/"))<2:
    pronouns = input(f"[ELIZA]: Please provide pronouns in the requested format. subject/object\n[{name}]: ")

subj = pronouns.split("/")[0].upper()
obj = pronouns.split("/")[1].upper()
