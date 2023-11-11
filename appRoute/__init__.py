import os
import subprocess
from flask import Flask, app, request, render_template
from werkzeug.utils import secure_filename


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'appRoute.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'pdf-file' in request.files:
            file = request.files['pdf-file']
            file.save(file.filename)
            # subprocess.run(["python", "main.py"], check=True)
        return render_template("index.html", name = file.filename)
            
    return app

if __name__ == '__main__':   
    app.run(debug=True)