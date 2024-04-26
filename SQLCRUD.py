import mysql.connector

hostname = "localhost"
username = "root"
password = ""
database = "sakila"
def getData(query):
  try:
    connection = mysql.connector.connect(host=hostname, user=username, password=password, database=database)
    # print("Connection successful!")
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results

  except mysql.connector.Error as err:
    print(f"Connection error: {err}")

  finally:
    if cursor:
      cursor.close()
    if connection:
      connection.close()
    print("Connection closed.")