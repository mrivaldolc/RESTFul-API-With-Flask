from datetime import *
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'edo_store'
mysql = MySQL(app)

@app.route('/')
def root():
    return "HELLOOO1234"

@app.route('/person')
def person():
    return jsonify ({'name' : 'popo',
                     'address' : 'loko'})

# show all
@app.route('/product', methods=['GET'])
def product():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM PRODUCT")

        # Get column names from cursor.description
        column_names = [i[0] for i in cursor.description]

        # Fetch data and format into list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))

        statuscode = 200
        status= {'messege': 'Data added successfully!',
                        'statuscode': statuscode,
                        'timestamp': datetime.now()}
        
        return jsonify(data, status)

        cursor.close()

# update
@app.route('/productupdate', methods=['POST'])
def productupdate():
    if request.method == 'POST':
        # Get data from request
        item_name = request.json['item_name']
        type_item = request.json['type_item']
        color = request.json['color']
        storage = request.json['storage']
        imei = request.json['imei']
        price = request.json['price']

        # Open connection and insert to db
        cursor = mysql.connection.cursor()
        sql = (f"INSERT INTO product(item_name, type_item, color, storage, imei, price) VALUES (%s, %s, %s, %s, %s, %s)")
        val = (item_name, type_item, color, storage, imei, price)
        cursor.execute(sql, val)                                                                                                                                                                      

        mysql.connection.commit()

        statuscode = 200
        return jsonify({'messege': 'Data added successfully!',
                        'statuscode': statuscode,
                        'timestamp': datetime.now()})
        cursor.close()

# detail
@app.route('/detailproduct', methods=['GET'])
def detailproduct():

    if 'id' in request.args:
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM product WHERE item_id = %s"
        val = (request.args['id'],)
        cursor.execute(sql, val)

        # Get column names from cursor.description
        column_names = [i[0] for i in cursor.description]

        # Fetch data and format into list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))

        statuscode = 200
        status= {'messege': 'Data added successfully!',
                        'statuscode': statuscode,
                        'timestamp': datetime.now()}

        return jsonify(data, status)
        cursor.close()


# edit 
@app.route('/editproduct', methods=['PUT'])
def editproduct():

    if 'id' in request.args:
        data = request.get_json()

        cursor = mysql.connection.cursor()
        sql = (f"UPDATE product SET item_name=%s, type_item=%s, color=%s ,storage=%s ,imei=%s ,price=%s WHERE item_id = %s")
        val = (data['item_name'], data['type_item'], data['color'] , data['storage'] , data['imei'] , data['price'], request.args['id'],)
        cursor.execute(sql,val)

        mysql.connection.commit()

        statuscode = 200
        return jsonify({'messege': 'Data updated successfully!',
                            'statuscode': statuscode,
                            'timestamp': datetime.now()})
        cursor.close()

# delete
@app.route('/deleteproduct', methods=['DELETE'])
def deleteproduct():
    if 'id' in request.args:
        cursor = mysql.connection.cursor()
        sql = (f"DELETE FROM product WHERE item_id = %s")
        val = (request.args['id'],)
        cursor.execute(sql, val)

        mysql.connection.commit()
        

        statuscode = 200
        return jsonify({'messege':'Data deleted successfully!',
                            'statuscode': statuscode,
                            'timestamp': datetime.now()})
    
        cursor.close()




if __name__ == '__main__':
    app.run(host="localhost", port=50, debug=True)