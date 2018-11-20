import pymysql.cursors
import json

class DBConnector:

    def __init__(self, host, user, password, db_name):
        self.connection = pymysql.connect(host=host,
                            user=user,
                            password=password,
                            db=db_name,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        self.cursor=self.connection.cursor()

    def inline_comments(self):
        sql = "SELECT * FROM inline_comments"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            row["written_on"] = str(row["written_on"])
        # inline_comments = json.dumps(result , default=str)
        return result

    def patches(self):
        sql = "SELECT * FROM patches"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            row["created"] = str(row["created"])
            row["committed"] = str(row["committed"])

        # patches = json.dumps(result , default=str)
        return result

    def patch_details(self):
        sql = "SELECT * FROM patch_details"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # patch_details = json.dumps(result , default=str)
        return result

    def people(self):
        sql = "SELECT * FROM people"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # people = json.dumps(result , default=str)
        return result

    def requests(self):
        sql = "SELECT * FROM requests"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            row["last_updated_on"] = str(row["last_updated_on"])
            row["created"] = str(row["created"])

        # requests = json.dumps(result , default=str)
        # return requests
        return result
    
    def request_detail(self):
        sql = "SELECT * FROM request_detail"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            row["created"] = str(row["created"])
            row["updated"] = str(row["updated"])

        # request_detail = json.dumps(result , default=str)
        # return request_detail
        return result
    
    def reviews(self):
        sql = "SELECT * FROM reviews"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # reviews = json.dumps(result , default=str)
        return result
    
    def review_comments(self):
        sql = "SELECT * FROM review_comments"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            row["created"] = str(row["created"])
        
        # review_comments = json.dumps(result , default=str)
        return result
    
# dbconnector = DBConnector('localhost','root','','gerrit_test')
