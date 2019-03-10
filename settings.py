import os


BASE_DIR = os.path.dirname((os.path.abspath(__file__)))


def rel(path):
    return os.path.join(BASE_DIR, path)


MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'market')
MONGO_URI = os.environ.get('MONGODB_URI')

TEMPLATE_DIRS = [
    rel('core/templates/'),
    rel('doors/templates/'),
    rel('contacts/templates'),
    rel('admin/templates/'),
]

STATIC_ROOT = rel('static')

MEDIA_ROOT = rel('media')
