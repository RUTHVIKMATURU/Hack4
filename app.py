from flask import Flask, request, jsonify, render_template
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def connect_db():
    conn = sqlite3.connect('elearning.db')
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_course', methods=['POST'])
def add_course():
    conn = connect_db()
    cursor = conn.cursor()

    title = request.form['title']
    description = request.form['description']
    reference_links = request.form.get('reference_links', '')
    question_papers = request.form.get('question_papers', '')

    if 'textbook' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['textbook']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
    else:
        filepath = ''

    cursor.execute("""
    INSERT INTO courses (title, description, textbook_file, reference_links, question_papers)
    VALUES (?, ?, ?, ?, ?)""",
    (title, description, filepath, reference_links, question_papers))
    
    conn.commit()
    conn.close()

    return jsonify({'message': 'Course added successfully!'}), 201

@app.route('/courses')
def courses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses_data = cursor.fetchall()
    conn.close()

    return render_template('courses.html', courses=courses_data)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
