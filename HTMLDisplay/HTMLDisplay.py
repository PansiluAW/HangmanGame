#this is to get all the stored records displayed as on a HTML file
#import modules
import mysql.connector
import webbrowser
#function
def html():
    data = []
    db = mysql.connector.connect(**connection)
    cursor = db.cursor()
    cursor.execute("SELECT * from records")
    result = cursor.fetchall()
    data.append("<tr><th>Player Name</th><th>Word Given</th><th>Turns Provided</th><th>Turns Used</th><th>Status</th></tr>")

    #creating html codes for each row
    for row in result:
        column1 = "<tr><td>%s</td>"%row[0]
        data.append(column1)
        column2 = "<td>%s</td>"%row[1]
        data.append(column2)
        column3 = "<td>%s</td>"%row[2]
        data.append(column3)
        column4 = "<td>%s</td>"%row[3]
        data.append(column4)
        column5 = "<td>%s</td></tr>"%row[4]
        data.append(column5)

    #converting the elements in 'data' list to a single string
    data_str = " ".join(data)
    #html codes
    html_codes = '''<!DOCTYPE html>
    <html>
    <head >
    <title>Hangman Game Results</title>
    </head>
    <body>
    <font  size = "10" face = "Fantasy" align = "center">
    <h1><marquee direction = "down" height = "100" width = "1000" scrollamount = "2"><center><u>Hangman</u></center></marquee></h1>
    <font  size = "5" face = "Arial" align = "center">
    <h2><center><u>Game Result History</u></center></h2>
    <table border = "3" align = "center">
    {}
    </table>
    </body>
    </html>
    '''.format(data_str)
    #handling the html file
    output = open("HangmanGameResults.html","w")
    output.write(html_codes)
    output.close()
    webbrowser.open("HangmanGameResults.html")

#dicitionary
connection = {"host":"localhost",
              "database":"player_records",
              "user":"root",
              "password":""}       
