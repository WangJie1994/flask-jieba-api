from flask import Flask
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import render_template
from flask_bootstrap import Bootstrap
from cutword import cut


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class SentenceForm(Form):
    sentence = StringField('What is the sentence?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    sentence = None
    form = SentenceForm()
    if form.validate_on_submit():
        sentence = form.sentence.data
        form.sentence.data = ''
        result = cut(sentence)
        print(result)
    return render_template('cut_api.html', form=form, sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)