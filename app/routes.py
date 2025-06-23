from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Poll

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    polls = Poll.query.all()
    return render_template('index.html', polls=polls)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        question = request.form['question']
        option1 = request.form['option1']
        option2 = request.form['option2']
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')

        poll = Poll(question=question, option1=option1, option2=option2,
                    option3=option3, option4=option4)
        db.session.add(poll)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('create.html')

@bp.route('/poll/<int:poll_id>', methods=['GET', 'POST'])
def vote(poll_id):
    poll = Poll.query.get_or_404(poll_id)

    if request.method == 'POST':
        choice = request.form['choice']
        if choice == '1':
            poll.votes1 += 1
        elif choice == '2':
            poll.votes2 += 1
        elif choice == '3':
            poll.votes3 += 1
        elif choice == '4':
            poll.votes4 += 1
        db.session.commit()
        return redirect(url_for('main.results', poll_id=poll.id))

    return render_template('vote.html', poll=poll)

@bp.route('/results/<int:poll_id>')
def results(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    return render_template('results.html', poll=poll)

@bp.route('/delete/<int:poll_id>', methods=['POST'])
def delete(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    db.session.delete(poll)
    db.session.commit()
    return redirect(url_for('main.index'))
