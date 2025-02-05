from flask import Flask, request, jsonify
import time
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        name TEXT PRIMARY KEY,
        quantity INTEGER
    )''')
    conn.commit()
    conn.close()

init_db()

# Log requests
def log_request(endpoint, data):
    print(f"[LOG] {endpoint} received: {data}")

# Transform endpoints
@app.route('/transform', methods=['POST'])
def transform():
    data = request.json
    log_request("transform", data)
    time.sleep(10)
    return jsonify({"message": "Transform received"}), 200

@app.route('/translation', methods=['POST'])
def translation():
    data = request.json
    log_request("translation", data)
    time.sleep(10)
    return jsonify({"message": "Translation received"}), 200

@app.route('/rotation', methods=['POST'])
def rotation():
    data = request.json
    log_request("rotation", data)
    time.sleep(10)
    return jsonify({"message": "Rotation received"}), 200

@app.route('/scale', methods=['POST'])
def scale():
    data = request.json
    log_request("scale", data)
    time.sleep(10)
    return jsonify({"message": "Scale received"}), 200

# File path endpoint
@app.route('/file-path', methods=['GET'])
def file_path():
    projectpath = request.args.get('projectpath', default=False, type=bool)
    if projectpath:
        return jsonify({"path": "/path/to/project"}), 200
    else:
        return jsonify({"path": "/path/to/file.blend"}), 200

# Inventory endpoints
@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.json
    log_request("add-item", data)
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (data["name"], data["quantity"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item added"}), 200

@app.route('/remove-item', methods=['POST'])
def remove_item():
    data = request.json
    log_request("remove-item", data)
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("DELETE FROM inventory WHERE name=?", (data["name"],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item removed"}), 200

@app.route('/update-quantity', methods=['POST'])
def update_quantity():
    data = request.json
    log_request("update-quantity", data)
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("UPDATE inventory SET quantity=? WHERE name=?", (data["new_quantity"], data["name"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Quantity updated"}), 200

if __name__ == '__main__':
    app.run(debug=True)
