import difflib
from difflib import get_close_matches

import mysql.connector
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary" )
dic = cursor.fetchall()
results = dict(dic)


def translate(w):     # In the difflib builtin functions there is a get_close_matches.. It matches
    w = w.lower()     # the entered wrong word with list of words and returns the right word.
    if w in results:
        return results[w]

    elif w.title() in results:
        return results[w.title()]

    elif w.upper() in results:
        return results[w.upper()]

    elif len(get_close_matches(w, results.keys())) > 0:
        result = input("Did you mean %s instead press Y for Yes and N for N0 ? " %get_close_matches(w,results.keys())[0])
        if result == "Y":
            return results[get_close_matches(w,results.keys())]
        elif result == "N":
            return "The word doesnt exist please give correct word"
        else:
            return "We didnt understand the entry"
    else:
        return "Word does not exist please enter another word"

word = input("Enter the word : ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else :
    print(output)



