from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.4gwwh2d.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/intro", methods=["POST"])
def intro_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    intro_list = list(db.intro.find({}, {'_id': False}))
    count = len(intro_list) + 1

    doc = {'num' : count , 'name': name_receive , 'comment': comment_receive}
    db.intro.insert_one(doc)

    return jsonify({'msg':'응원 감사합니다!!'})



@app.route("/intro", methods=["GET"])
def intro_get():
    intro_list = list(db.intro.find({}, {'_id': False}))
    return jsonify({'intro':intro_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)