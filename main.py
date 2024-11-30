from app import create_app
from config import get_runtime_config

app=create_app(get_runtime_config())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7000')
