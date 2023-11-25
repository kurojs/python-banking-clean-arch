import os

APP_NAME = os.getenv('APP_NAME', 'BankApp')
APP_VERSION = os.getenv('APP_VERSION', '0.0.1')

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', '5432'))
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'postgres')

DB_DRIVER = os.environ.get('DB_DRIVER', 'postgresql')
DB_URI = os.environ.get('DB_URI',
                        f'{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
