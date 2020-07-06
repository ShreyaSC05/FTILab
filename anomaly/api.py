from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  anomaly import edit_config


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/event.db'
db = SQLAlchemy(app)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/update_config', methods=['POST'])
    def update_config(id):
        edit_config(id, data)

    @app.route('/add_config', methods=['POST'])
    def add_config():
        add_config(data)

    @app.route('/delete_config', methods=['POST'])
    def delete_config(id):
        delete_config(id)


app = create_app()

if __name__ == '__main__':
        app.run(debug=True)

