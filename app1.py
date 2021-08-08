import json
import difflib
from difflib import get_close_matches
data = json.load(open("Project-1/data.json"))

def translate(w):
    w = w.lower()

    if w in data: # checking the word  # In the difflib function there is 
        return(data[w][0])
    
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if yes and N for No: " %get_close_matches(w,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w,data.keys())[0]][0]
        elif yn == 'N':
            return "Word doesnt exist please double check it"
        else:
            return "We did not understand the query"
    

    else :             
        return "The word does not exist.Pls double check it "

word = str(input("Enter the word: "))

print(translate(word))