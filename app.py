from flask import Flask, render_template, jsonify, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb", 27017)
db = client["deliveries"]
collection = db["Items"]


@app.route('/', methods=["GET"])
def base_page():
    return render_template('welcome.html')

@app.route('/client')
def client_route():
    return render_template('client.html')


@app.route("/supplier", methods=["GET"])
def render_insert_form():
    return render_template("supplier.html")


@app.route('/supplier', methods=['POST'])
def insert_data():
    try:
        data = request.get_json()
        print(data)
        if data and "custumer_name" in data and "package_id" in data and "custumer_email" in data:
            # Insert data into the MongoDB collection
            collection.insert_one({
                "custumer_name": data["custumer_name"],
                "package_id": data["package_id"],
                "custumer_email": data["custumer_email"]
            })
            return jsonify({"status": "success", "message": "Data inserted successfully!"})
        else:
            return jsonify({"status": "error", "message": "Invalid data format!"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    


@app.route('/courier')
def courier_route():
    return 'Courier Page'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")