from flask import Flask, render_template, request

app = Flask(__name__)

# Prime logic included here
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    primes = None
    x_value = None
    if request.method == 'POST':
        x_value = int(request.form['number'])
        primes = []
        num = x_value + 1
        while len(primes) < 10:
            if is_prime(num):
                primes.append(num)
            num += 1
    return render_template('index.html', primes=primes, x_value=x_value)

if __name__ == '__main__':
    app.run(debug=True)