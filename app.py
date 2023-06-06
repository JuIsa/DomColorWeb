from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
app = Flask(__name__)
# app.config['/']

app.secret_key= 'asd'

@app.route('/')
def index():
    return render_template('index.html',message = 'Enter Text')

# @app.route('/dom',methods=['POST','GET'])
# def greet():
#     words = str(request.form['text_input'])
#     words = words.split()
#     result = ''
#     for word in words:
#         result+=emphasize(word)+' '
#     return render_template('index.html',message = result)

@app.route('/dom', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


def emphasize(word):
    lens = [10,6,4,2]
    places = [4,2,1,0]
    for l in range(len(lens)):
        if len(word)>=lens[l]:
            return '<b class="light">'+word.replace(word[places[l]],word[places[l]]+'</b>')
    return '<b class="light">'+word+'</b>'
 