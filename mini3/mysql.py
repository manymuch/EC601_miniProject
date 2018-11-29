import pymysql


#connect to the dataset and create the table if not exist and retrun the table cursor
def connect_mysql(LOCALHOST = 'localhost',USER = 'twitterweb',PASSWARD = 'bu_ec601',DATABASE = 'twitter'):
    con = pymysql.connect(LOCALHOST,USER,PASSWARD,DATABASE,autocommit=True)
    CursorObject = con.cursor()
    sqlQuery = """CREATE TABLE IF NOT EXISTS twitter_images(id int not null auto_increment primary key,username varchar(32) not null,twittername varchar(32) not null,imageurl varchar(2083) not null,label varchar(32) not null);"""
    CursorObject.execute(sqlQuery)
    return CursorObject

def printall(CursorObject):
    sqlQuery = "show tables"
    CursorObject.execute(sqlQuery)
    print('\n\n\nmysql output:')
    rows = CursorObject.fetchall()
    for row in rows:
        print(row)

    sqlQuery = "select * from twitter_images"
    CursorObject.execute(sqlQuery)
    rows = CursorObject.fetchall()
    for row in rows:
        print(row)

def insert(USER_NAME,TWITTER_NAME,URL,LABEL):
    sqlQuery = "INSERT INTO twitter_images VALUES(NULL,\'%s\',\'%s\',\'%s\',\'%s\')" % (USER_NAME,TWITTER_NAME,URL,LABEL)
    sqlQuery2 = "INSERT INTO twitter_images VALUES(NULL,'tony','@jeremy','http://helow.word','elephant')"
    CursorObject.execute(sqlQuery)


if __name__ == '__main__':
    CursorObject = connect_mysql()
    insert("tony","@jeremy",'http://s/sdfsdfwew',"fat2")
    printall(CursorObject)
