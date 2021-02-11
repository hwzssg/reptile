from flask import Flask
import time

app = Flask(__name__)

@app.route('/wang1')
def index_wang1():
    time.sleep(2)
    return 'hello wang1'

@app.route('/wang2')
def index_wang2():
    time.sleep(2)
    return 'hello wang2'

@app.route('/wang3')
def index_wang3():
    time.sleep(2)
    return 'hello wang3'

if __name__ == '__main__':
    app.run(threaded=True)