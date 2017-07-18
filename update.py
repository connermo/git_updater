from flask import Flask
import os
app = Flask(__name__)

@app.route('/update/<name>', methods=['GET', 'POST'])
def update():
    tmp = os.popen('/opt/git/update.sh %s' % name).readlines()
    return '\n'.join(tmp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')
