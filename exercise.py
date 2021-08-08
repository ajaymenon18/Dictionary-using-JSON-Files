import mysql.connector
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word )
results = cursor.fetchall()

dic = dict(results)
print(dic)
print(type(dic))
print(type(results[0][1]))

if results:
    for result in results:
        print(result[0])
else:
    print("No word found ! ")



