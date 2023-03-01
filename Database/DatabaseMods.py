#this is for the function to store the player information and other records in a table in the database
#import sql connector
import mysql.connector

#function to store data in a table in the database    
def store(name,word,turns_provided,turns_used,status):
    "this is for creating a new database with a table named records and storing the data in it"
    #create new databse
    db = mysql.connector.connect(**connection_new)
    if db:
        print()
        print("_______Connection Established with the Database Server_______")
    else:
        print()
        print("_____Database Server Connection Failed_____")
    cursor = db.cursor()
    create_database = "CREATE DATABASE IF NOT EXISTS player_records"
    cursor.execute(create_database)
    db.commit()
    db.close()

    #create new table in the database
    db = mysql.connector.connect(**connection)
    cursor = db.cursor()
    create_table = "CREATE TABLE IF NOT EXISTS records(name VARCHAR(255), word VARCHAR(255), turnsProvided INT(2), turnsUsed INT(2), status VARCHAR (5));"
    cursor.execute(create_table)
    db.commit()

    #import old database records
    cursor.execute('SELECT count(*) FROM records')
    restore = cursor.fetchall()
    if restore[0][0] == 0:
        cursor.execute("INSERT INTO `records` (`name`, `word`, `turnsProvided`, `turnsUsed`, `status`) VALUES ('Susan De Silva', 'school', 6, 3, 'won'),('Alex Ernest', 'speaker', 7, 3, 'won'),('Alex Ernest', 'keyboard', 8, 8, 'lost'),('Aritha Wijeweera', 'bottle', 6, 6, 'lost'),('Aryton Senna', 'eagle', 5, 1, 'won'),('Aryton Senna', 'speaker', 7, 7, 'lost'),('Aryton Senna', 'ostrich', 7, 1, 'won'),('Suarez De Villiers', 'eagle', 5, 3, 'won'),('Suarez De Villiers', 'ostrich', 7, 7, 'lost'),('Suarez De Villiers', 'cupboard', 8, 1, 'won');")
        
    #insert data
    insert = "INSERT INTO records(name, word, turnsProvided, turnsUsed, status) VALUES(%s,%s,%s,%s,%s);"
    values = (name,word,turns_provided,turns_used,status)
    cursor.execute(insert,values)
    db.commit()
    print("\n~~~~~~~~~~~~~~~~~",cursor.rowcount,"Player record was added ~~~~~~~~~~~~~~~~~\n")
    db.close()

#this is for displaying the records stored in the database
def display():
    "This is for displaying the records stored in the database"
    total_games = 0
    total_wins = 0
    total_losses = 0
    db = mysql.connector.connect(**connection)
    cursor = db.cursor()
    #get the total games played
    cursor.execute('SELECT count(*) FROM records')
    total_games = (cursor.fetchall()[0])[0]
    
    #get the total wins according to the stored records
    cursor.execute('SELECT count(*) FROM records WHERE status = "won"')
    total_wins = (cursor.fetchall()[0])[0]

    #get the total losses according to the stored records
    cursor.execute('SELECT count(*) FROM records WHERE status = "lost"')
    total_losses = (cursor.fetchall()[0])[0]

    #display the collected data
    print("____________________________________________________")
    print("Total Games Played\tTotal Wins\tTotal Losses ")
    print("____________________________________________________")
    print(" ",total_games,"\t\t\t",total_wins,"\t\t\t",total_losses)
    return
    


#database connection
connection = {"host":"localhost",
              "database":"player_records",
              "user":"root",
              "password":""}

connection_new = {"host":"localhost",              
              "user":"root",
              "password":""}

