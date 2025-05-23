from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/'

def init_db():
    with sqlite3.connect('dogs.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS dogs (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          age INTEGER NOT NULL,
                          photo TEXT NOT NULL,
                          with_other_dogs BOOLEAN NOT NULL,
                          with_kids BOOLEAN NOT NULL,
                          owner_name TEXT NOT NULL,
                          contact_email TEXT NOT NULL,
                          date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_dog', methods=['GET', 'POST'])
def post_dog():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        with_other_dogs = 'with_other_dogs' in request.form
        with_kids = 'with_kids' in request.form
        owner_name = request.form['owner_name']
        contact_email = request.form['contact_email']
        
        photo = request.files['photo']
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
        photo.save(photo_path)

        with sqlite3.connect('dogs.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO dogs (name, age, photo, with_other_dogs, with_kids, owner_name, contact_email) 
                              VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                           (name, age, photo.filename, with_other_dogs, with_kids, owner_name, contact_email))
            conn.commit()
        
        return redirect(url_for('feed'))

    return render_template('post_dog.html')

@app.route('/feed')
def feed():
    with sqlite3.connect('dogs.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dogs ORDER BY date_added DESC')
        dogs = cursor.fetchall()
    
    return render_template('feed.html', dogs=dogs)

@app.route('/adopt/<int:dog_id>')
def adopt(dog_id):
    with sqlite3.connect('dogs.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT owner_name, contact_email FROM dogs WHERE id = ?', (dog_id,))
        dog_info = cursor.fetchone()
    
    return render_template('adopt.html', dog_info=dog_info)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
