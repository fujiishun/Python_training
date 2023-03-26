from flask import Flask, render_template, request
app = Flask(__name__)
###(index)###
#index
@app.route('/')
def index():
    data = {
        'test1': 'testです',
        'test2': 'test2',
        'title': ['title1', 'title2', 'title3']
    }
    return render_template('index.html',data=data)

#画像アップロード
@app.route('/upload',methods=['POST'])
def upload():
    img_file = request.files['img_file']
    print(img_file.filename)
    path = f'./static/{img_file.filename}'
    img_file.save(path)
    return render_template("index.html",img_url=path)

###()###
#値の挿入
@app.route('/home/<string:user_name>/<int:age>')
def home(user_name,age):
    login_user = {
        'name':user_name,
        'age':age
    }
    return render_template('home.html',login_user=login_user)
###(postform)###
#送信フォーム
@app.route('/postform', methods=['GET', 'POST'])
def postform():
    if request.method == 'GET':
        return render_template('postform.html')
    if request.method == 'POST':
        print('POSTデータ受け取ったので処理します。')
        req = request.form['data']
        return render_template('getform.html', req=req)

app.run(port=8000, debug=True)