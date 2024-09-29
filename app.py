from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        return render_template('index.html', n = n, a = a)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
##changes made to check codefix branch
## 2nd Change for codefix branch