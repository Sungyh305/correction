from flask import Flask, render_template, request
from hanspell import spell_checker

app = Flask(__name__)

chat_history = []  # 대화 내역 리스트 초기화

@app.route('/', methods=['GET', 'POST'])
def index():
    global chat_history  # 전역 변수 사용

    if request.method == 'POST':
        user_input = request.form['input_text']

        # Hanspell 라이브러리를 사용하여 입력 문장의 맞춤법을 교정합니다.
        corrected_input = spell_checker.check(user_input).checked

        # 대화 내역에 사용자 입력과 교정된 입력 추가
        chat_history.append(f"사용자: {user_input}")
        chat_history.append(f"교정된 입력: {corrected_input}")

    return render_template('chat.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
