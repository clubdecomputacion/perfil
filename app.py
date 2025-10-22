from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Consultar el API de Random User
        response = requests.get('https://randomuser.me/api/')
        response.raise_for_status()
        
        data = response.json()
        user = data['results'][0]
        
        return render_template('profile.html', user=user)
    
    except requests.RequestException as e:
        return f"Error al consultar el API: {str(e)}", 500
    except (KeyError, IndexError) as e:
        return f"Error al procesar los datos: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

