from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'test_upload'
CORS(app)

@app.route('/api/upload',methods=['POST','GET'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
    return jsonify({'message':'upload success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000,debug=True)
