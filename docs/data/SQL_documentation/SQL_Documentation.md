# How to connect to the databae build in MySQL

## 1. Conect to the server from the terminal

This instructions are creatted to conncet to the remote server on a linux terminal. 

### 1.1 Type the following command with your username and the mysql_server_ip

Please always follow this format:

```mysql -u username -h mysql_server_ip -p```

For example:
```
mysql -u sql7582498 -h sql7.freesqldatabase.com -p
```

### 1.2 Type your password

Next you need to typr your password

## 2. Conect to the server from python or a notebook

### 2.1 Create a conector

```
import mysql.connector
cnx = mysql.connector.connect(user='user_Name', password='password',
                              host='127.0.0.1',
                              database='data_basename')
cursor = cnx.cursor()
```
### 2.2 Make queries
```
query = ("SELECT * FROM database")
cursor.execute(query, (hire_start, hire_end))
```
# Referencs
1. Create a free MySQL database: https://www.youtube.com/watch?v=TMGHOW8Hzvw
2. Connect to a remote MySQL datbase: https://phoenixnap.com/kb/mysql-remote-connection
3. MySQL connector: https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
