from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.secret_key = "b'\xa9\xe8\xb2\x12\x8f\xf3\xda\xbc\xd9\x0e\xaf\xb7\x13\xd1\xb0\xe9\x7a\xc4\x2b\x3c\x1a\x1d\x9e\x8f'"


@app.route('/')
def home():
    return render_template('index2.html', title='Home1', heading='Welcome to the website', content='This is a simple '
                                                                                                  'website built using'
                                                                                                  ' Flask')

@app.route("/about")
def about():
    return 'This is the about page.'


@app.route("/contact")
def contact():
    return 'Contact us at: contact@example.com'


@app.route('/conditional')
def conditional():
    condition = False
    return render_template('conditional.html', title='Conditional', heading='Conditional content', content='This is a '
                                                                                                           'conditional content',
                           condition=condition)


@app.route('/list')
def list():
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index2.html', title='List', heading='List of items', content='This is a list of items',
                           items=items)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age', [NumberRange(min=0, max=120)])


data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]


@app.route('/form')
def submit():
    form = MyForm()
    return render_template('form.html', form=form)


@app.route('/update', methods=['POST'])
def update():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        data.append({"name": name, "age": age})
    return render_template('index2.html', form=form, data=data)


if __name__ == '__main__':
    app.run()
