from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def shop():
   return render_template('cart.html')

@app.route('/checkout',methods = ['POST', 'GET'])
def cart():
   if request.method == 'POST':
      cart = request.form
      return render_template("checkout.html",checkout = checkout)

if __name__ == '__main__':
   app.run(debug = True)
