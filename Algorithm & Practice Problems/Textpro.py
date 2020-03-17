def sentence_maker(pharse):
    interrogative = ("How", "What", "Why")
    cap = pharse.capitalize()
    if (cap.startswith(interrogative)):
        return "{}?".format(cap)
    else:
        return "{}.".format(cap)
    

string = ""
sentences = []

while(string != "/end"):
    string = input("Enter a sentence ")
    new_string = sentence_maker(string)
    sentences.append(new_string)

sentences.pop()

print(' '.join(sentences))