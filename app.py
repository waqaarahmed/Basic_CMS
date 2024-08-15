
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Content

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        content = Content(title=title, body=body)
        db.session.add(content)
        db.session.commit()
        flash('Content created successfully!')
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    content = Content.query.get_or_404(id)
    if request.method == 'POST'):
        content.title = request.form['title']
        content.body = request.form['body']
        db.session.commit()
        flash('Content updated successfully!')
        return redirect(url_for('index'))
    return render_template('update.html', content=content)



