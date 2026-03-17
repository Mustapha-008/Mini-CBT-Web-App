from flask import Flask, render_template, request, redirect, url_for, session
from models import Question, CBT
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# Sample questions
questions_list = [
    Question("What is the capital of Nigeria?", ["Lagos", "Abuja", "Kano", "Port Harcourt"], "Abuja"),
    Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    Question("Which language is this app built with?", ["Java", "Python", "C++", "Ruby"], "Python"),
    Question("What does HTML stand for?", ["Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language", "Hyperlinking Text Mark Language"], "Hyper Text Markup Language"),
    Question("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], "Mars")
]

@app.route('/')
def index():
    # Initialize CBT session
    cbt = CBT(questions_list)
    session['cbt'] = {
        'current_index': 0,
        'score': 0,
        'start_time': datetime.now().isoformat()
    }
    return redirect(url_for('question'))

@app.route('/question', methods=['GET', 'POST'])
def question():
    cbt_data = session.get('cbt', None)
    if not cbt_data:
        return redirect(url_for('index'))

    current_index = cbt_data['current_index']
    score = cbt_data['score']
    start_time = datetime.fromisoformat(cbt_data['start_time'])

    if current_index >= len(questions_list):
        # Test finished
        end_time = datetime.now()
        duration = end_time - start_time
        return redirect(url_for('result'))

    question = questions_list[current_index]

    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option == question.answer:
            score += 1
        current_index += 1
        session['cbt'] = {
            'current_index': current_index,
            'score': score,
            'start_time': start_time.isoformat()
        }
        if current_index >= len(questions_list):
            return redirect(url_for('result'))
        else:
            return redirect(url_for('question'))

    return render_template('index.html', question=question, question_number=current_index + 1, total_questions=len(questions_list))

@app.route('/result')
def result():
    cbt_data = session.get('cbt', None)
    if not cbt_data:
        return redirect(url_for('index'))

    score = cbt_data['score']
    start_time = datetime.fromisoformat(cbt_data['start_time'])
    end_time = datetime.now()
    duration = end_time - start_time

    return render_template('result.html', score=score, total=len(questions_list), timestamp=end_time.strftime("%Y-%m-%d %H:%M:%S"), duration=str(duration).split('.')[0])

if __name__ == '__main__':
    app.run(debug=True)