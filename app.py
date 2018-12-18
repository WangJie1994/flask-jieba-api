from flask import Flask
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import render_template
from flask_bootstrap import Bootstrap
from cutword import cut
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class SentenceForm(Form):
    sentence = StringField('What is the sentence you want to cut?', validators=[Required()])
    submit = SubmitField('Submit')


# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cut', methods=['GET', 'POST'])
def cut_page():
    sentence = None
    result = None
    form = SentenceForm()
    if form.validate_on_submit():
        sentence = form.sentence.data
        form.sentence.data = ''
        result = cut(sentence)
        # print(result)
    return render_template('cut_api.html', form=form, sentence=sentence, result=result)


# @app.route('/cut/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})


# @app.route('/cut/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = list(filter(lambda t: t['id'] == task_id, tasks))
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/cut/api/v1.0', methods=['POST']) # post方法测试
def cut_handler():
    if not request.json or not 'sentence' in request.json:
        abort(400)
    sentence = request.json.get('sentence')
    cut_result = cut(sentence)
    return jsonify({'result': cut_result})


if __name__ == '__main__':
    app.run(debug=True)
