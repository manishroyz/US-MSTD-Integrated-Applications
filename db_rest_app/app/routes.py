# from flask import Flask, render_template
from app import app
from flask import request, jsonify
import pymysql
import json



class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "admin1234"
        db = "usmstd"

        self.connectionObj = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cursorObj = self.connectionObj.cursor()

    def get_data(self):
        sql_query = "SELECT collect_date, tof_s1, tof_s2, tof_s3, tof_s4, temp_s1, temp_s2, temp_s3, temp_s4, " \
                    "tc1, tc2, tc3, tc4, tc5, tc6 FROM experimental_data"
        self.cursorObj.execute(sql_query)
        result = list(self.cursorObj.fetchall())

        # Converts all decimal values in the dictionary to a string
        result_stringified = [dict([key, str(value)] for key, value in dicts.items()) for dicts in result]

        return result_stringified

    def insert_data(self, json_data):
        # print(json_data)
        collect_date = json_data["collect_date"]
        tof_s1 = json_data["tof_s1"]
        tof_s2 = json_data["tof_s2"]
        tof_s3 = json_data["tof_s3"]
        tof_s4 = json_data["tof_s4"]
        temp_s1 = json_data["temp_s1"]
        temp_s2 = json_data["temp_s2"]
        temp_s3 = json_data["temp_s3"]
        temp_s4 = json_data["temp_s4"]
        tc1 = json_data["tc1"]
        tc2 = json_data["tc2"]
        tc3 = json_data["tc3"]
        tc4 = json_data["tc4"]
        tc5 = json_data["tc5"]
        tc6 = json_data["tc6"]

        sql_query = "INSERT INTO experimental_data() VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (collect_date, tof_s1, tof_s2, tof_s3, tof_s4, temp_s1, temp_s2, temp_s3, temp_s4, tc1, tc2,
                 tc3, tc4, tc5, tc6)

        self.cursorObj.execute(sql_query, data)
        self.connectionObj.commit()
        resp = jsonify('Data added successfully!!!')

        return resp


# Class place holder for ORM implementation
# class dataVals:
#     def __init__(self, firstname, lastname, gender):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.gender = gender



@app.route('/')
@app.route('/get_data')
def get_db_data():
    db = Database()
    fetched_data = db.get_data()
    print(fetched_data)

    # converts to JSON
    fetched_data_json = json.dumps(fetched_data)

    return fetched_data_json


@app.route('/add', methods=['POST'])
def add_data_to_db():
    _json = request.json
    db = Database()
    ret_msg = db.insert_data(_json)
    return ret_msg



