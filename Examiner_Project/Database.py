import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "kubanek",
    database = "mydata"
    )


mycursor = db.cursor()

def insert_value(spanish_word, english_word):
    mycursor.execute("INSERT INTO new_vocabulary (spanish, english) VALUES (%s, %s)", (spanish_word, english_word))
    db.commit()
    print(f'The word {spanish_word} with translation {english_word} was added.')

def show_vocabulary():

    print ('In the vocabulary are values:', '\n')
    mycursor.execute("SELECT * FROM new_vocabulary")
    for x in mycursor.fetchall():
        print(x)

def return_words():

    mycursor.execute("SELECT * FROM new_vocabulary ORDER BY RAND() LIMIT 1")
    word = mycursor.fetchone()

    return word[0:2]

#CREATE TABLE
#mycursor.execute("CREATE TABLE Vocabulary (spanish VARCHAR(50), enslish VARCHAR(50), wordID int PRIMARY KEY AUTO_INCREMENT)")

#SHOW TABLES
#mycursor.execute("SHOW TABLES")
#for databases in mycursor:
#    print (databases)

#INSERT
#mycursor.execute("INSERT INTO Vocabulary (spanish, english) VALUES (%s, %s)", ("hola", "hello"))
#DELETE
#mycursor.execute("DELETE FROM Vocabulary WHERE wordID = '2'")

#spanish_word = "amigo"
#english_word = "friend"

#mycursor.execute("INSERT INTO Vocabulary (spanish, english) VALUES (%s, %s)", (spanish_word, english_word))
