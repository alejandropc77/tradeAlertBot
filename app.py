from flask import Flask
import trade_script
app = Flask(__name__)

@app.route('/')
def trade():
    trade_script()
    return ''

if __name__ == '__main__':
    app.debug = True
    app.run()