# Perfil: Consumo de API con Flask

Este proyecto es un ejemplo educativo que demuestra cómo consumir una API REST y mostrar los datos en una aplicación web usando Flask. Perfecto para estudiantes que están aprendiendo sobre desarrollo web backend y APIs.

## Características

- Consume datos de la API [Random User](https://randomuser.me/)
- Muestra un perfil de usuario con información personal
- Diseño responsive y moderno
- Manejo de errores en las peticiones API
- Fácil de extender y personalizar

## Configuración del Proyecto

1. Crear un *Fork* del repositorio

    - Ingresa a GitHub con tu cuenta, y ve al repositorio [perfil](https://github.com/clubdecomputacion/perfil).
    - Haz clic en el botón **Fork** y confirma la creación del mismo.

2. Clona tu repositorio

    ```bash
    git clone https://github.com/tu-usuario/perfil.git
    cd perfil
    ```

3. Configura Entorno Virtual

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Instala las dependencias

    ```bash
    pip install -r requirements.txt
    ```

5. Ejecuta la aplicación

    ```bash
    python app.py
    ```

    La aplicación estará disponible en: `http://localhost:5000`

## Estructura del Proyecto

```
perfil/
├── app.py                 # Aplicación principal Flask
├── templates/
│   └── profile.html      # Template HTML del perfil
├── static/
│   └── css/
│       └── style.css     # Estilos CSS
└── README.md
```

## Mejoras Sugeridas

1. Mejora la gestión de errores

```python
# Agregar más tipos de excepciones
except requests.Timeout:
    return "Error: Tiempo de espera agotado", 408
except requests.ConnectionError:
    return "Error: Problema de conexión", 503
```

2. Guarda en cache las peticiones realizadas

```python
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=60)  # Cache por 60 segundos
def index():
    # tu código aquí
```

3. Utiliza variables de entorno

```python
import os

API_URL = os.getenv('API_URL', 'https://randomuser.me/api/')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
```

4. Agrega pruebas unitarios

```python
# tests/test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_index_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
```

5. Implementa logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    logger.info('Solicitud recibida en la página principal')
    # tu código aquí
```

6. Adiciona más end-points

```python
@app.route('/user/<user_id>')
def user_profile(user_id):
    # Obtener usuario específico por ID
    pass

@app.route('/multiple')
def multiple_users():
    # Mostrar múltiples usuarios
    response = requests.get('https://randomuser.me/api/?results=5')
```

7. Agrega una base de datos

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    # más campos...
```

8. Incluye un mecanismo de autenticación

```python
from flask_login import LoginManager, UserMixin, login_required

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/dashboard')
@login_required
def dashboard():
    return "Página protegida"
```

9. Utiliza un API REST propio

```python
@app.route('/api/profile')
def api_profile():
    user_data = {
        'name': f"{user['name']['first']} {user['name']['last']}",
        'email': user['email'],
        # más datos...
    }
    return jsonify(user_data)
```

10. Agrega soporte para internacionalización

```python
from flask_babel import Babel, gettext

babel = Babel(app)

@app.route('/')
def index():
    return render_template('profile.html', 
                         user=user, 
                         title=gettext('User Profile'))
```

11. Automatiza la documentación del API

```python
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Profile API"}
)
```

12. Utiliza contenedores

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Recursos Adicionales

- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/)
- [Random User API Documentation](https://randomuser.me/documentation)

