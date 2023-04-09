from flask import Flask, render_template, redirect, request, session

app =  Flask(__name__)
app.secret_key = 'porkchop and cheese'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['power_level'] = request.form['power_level']
    session['fav_language'] = request.form['fav_language']
    session['msg'] = request.form['msg']
    # print(request.form['name'])
    # print(request.form['power_level'])
    # print(request.form['fav_language'])
    # print(request.form['msg'])
    return redirect('/result')

if __name__ == "__main__":
    app.run(debug=True)