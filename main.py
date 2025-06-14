from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>스포츠 지도사 CBT 사이트에 오신 걸 환영합니다!</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
