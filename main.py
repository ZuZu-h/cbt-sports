from flask import Flask, request, render_template_string

app = Flask(__name__)

question = {
    "text": "다음 중 스포츠의 기능으로 옳지 않은 것은?",
    "options": ["사회 통합 기능", "경제적 기능", "환경 파괴 기능", "교육적 기능"],
    "answer": 3
}

html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>CBT 문제</title>
</head>
<body>
    <h2>{{ q['text'] }}</h2>
    <form method="POST">
        {% for opt in q['options'] %}
            <label>
                <input type="radio" name="choice" value="{{ loop.index }}" required>
                {{ opt }}
            </label><br>
        {% endfor %}
        <button type="submit">제출</button>
    </form>

    {% if submitted %}
        <hr>
        {% if correct %}
            <p style="color:green;">✅ 정답입니다!</p>
        {% else %}
            <p style="color:red;">❌ 오답입니다. 정답은 <strong>{{ q['options'][q['answer'] - 1] }}</strong>입니다.</p>
        {% endif %}
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def quiz():
    submitted = False
    correct = False
    if request.method == "POST":
        choice = int(request.form.get("choice"))
        submitted = True
        correct = (choice == question["answer"])
    return render_template_string(html, q=question, submitted=submitted, correct=correct)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

