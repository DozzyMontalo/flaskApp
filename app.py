from flask import Flask
from flask_migrate import Migrate
from extention import db
import logging


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Breezy91@localhost/hoteldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Initialize SQLAlchemy extension
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    from routes import *  # Import routes here to avoid circular import
    app.run(debug=True)


# Configure logging
app.logger.setLevel(logging.DEBUG)  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
file_handler = logging.FileHandler('app.log')  # Create a log file
file_handler.setLevel(logging.INFO)  # Set log level for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)  # Set formatting for log messages
app.logger.addHandler(file_handler)  # Add the file handler to the logger