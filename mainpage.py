from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def items():
   return render_template('home.html')

@app.route('/checkout',methods = ['POST', 'GET'])
def cart():
   if request.method == 'POST':
      cart = request.form
      return render_template("checkout.html",checkout = checkout)

if __name__ == '__main__':
   app.run(debug = True)
