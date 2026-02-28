from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from init_db import init_db

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'database.db')

# Ensure DB is initialized before first request
if not os.path.exists(db_path):
    init_db()

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in todos])

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.json
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Text is required'}), 400
    
    conn = get_db_connection()
    cursor = conn.execute('INSERT INTO todos (text, completed) VALUES (?, ?)', (text, False))
    conn.commit()
    new_id = cursor.lastrowid
    
    new_todo = conn.execute('SELECT * FROM todos WHERE id = ?', (new_id,)).fetchone()
    conn.close()
    
    return jsonify(dict(new_todo)), 201

@app.route('/api/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.json
    conn = get_db_connection()
    todo = conn.execute('SELECT * FROM todos WHERE id = ?', (id,)).fetchone()
    if todo is None:
        conn.close()
        return jsonify({'error': 'Todo not found'}), 404
        
    text = data.get('text', todo['text'])
    completed = data.get('completed', todo['completed'])
    
    completed_val = 1 if completed else 0
    
    conn.execute('UPDATE todos SET text = ?, completed = ? WHERE id = ?', (text, completed_val, id))
    conn.commit()
    
    updated_todo = conn.execute('SELECT * FROM todos WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    return jsonify(dict(updated_todo))

@app.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=8000) # Changed port to 8000
