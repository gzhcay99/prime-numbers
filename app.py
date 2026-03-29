import os
from flask import Flask, render_template, request

app = Flask(__name__)

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_next_10_primes(x):
    """Returns the next 10 prime numbers larger than X."""
    primes = []
    num = x + 1
    while len(primes) < 10:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

@app.route('/', methods=['GET', 'POST'])
def index():
    primes = None
    x_value = None
    if request.method == 'POST':
        try:
            x_value = int(request.form['number'])
            primes = get_next_10_primes(x_value)
        except ValueError:
            primes = "Please enter a valid integer."
            
    return render_template('index.html', primes=primes, x_value=x_value)

if __name__ == '__main__':
    # PORT is required for public servers like Render/Heroku
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)