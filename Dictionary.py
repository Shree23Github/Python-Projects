import json 
from difflib import get_close_matches

data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0:
        yesno= input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0])
        if yesno=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yesno=="N":
            return "The Word doesn't match,please double check your input"
        else:
            return "We didn't understand your entry"
    else:
        return "The Word doesn't exist,please double check your input"
    
    word=input("Enter your word: ")
    output=translate(word)
    if type(output)==list:
        for item in output:
            print(item)
        else:
            print(output)
