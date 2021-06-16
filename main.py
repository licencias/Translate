from flask import Flask, render_template, request, redirect, url_for
import google_trans_new
from google_trans_new import google_translator


app = Flask(__name__)

translator = google_translator()

#define
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message',methods=['POST'])
def form_prod():
    if(request.method == 'POST'):
        print(request.form['mensaje'])
        trad = request.form['mensaje']
        data = translator.translate(trad,lang_tgt='en')
        print(data)
        return render_template('index.html',datos = data)

if __name__ == '__main__':
    app.run()