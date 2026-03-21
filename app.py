import os
import jwt
import datetime
import requests
from flask import Flask, request, jsonify
from functools import wraps
from dotenv import load_dotenv

# Carga de variables de entorno desde el archivo .env
load_dotenv()

# --- VALIDACIÓN CRÍTICA DE SEGURIDAD ---
JWT_SECRET = os.getenv('JWT_SECRET')
if not JWT_SECRET:
    raise RuntimeError(
        "ERROR: No se encontró 'JWT_SECRET' en las variables de entorno. "
        "Por seguridad, la API no puede iniciar sin una clave de firma válida."
    )

app = Flask(__name__)
app.config['SECRET_KEY'] = JWT_SECRET
VT_API_KEY = os.getenv('VT_API_KEY')
PORT = int(os.getenv('PORT', 8080))

# "Base de datos" interna de usuarios
USERS = {
    "alan": "alan123",
    "diego": "diego123",
    "oscar": "oscar123"
}

# --- DECORADOR PARA VALIDACIÓN DE TOKEN BEARER ---
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Acceso denegado: Token no encontrado'}), 401

        try:
            # Validación de firma y tiempo de expiración
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'El token ha expirado'}), 401
        except Exception:
            return jsonify({'message': 'Token inválido o corrupto'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# --- RUTAS DE LA API ---

@app.route('/api/v1/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({"message": "Faltan credenciales"}), 400

    user = auth.get('username')
    password = auth.get('password')

    if USERS.get(user) == password:
        # Generación del token con 1 hora de validez
        token = jwt.encode({
            'user': user,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({'token': token, 'type': 'Bearer'})

    return jsonify({"message": "Credenciales inválidas"}), 401

@app.route('/api/v1/status', methods=['GET'])
@token_required
def get_status(current_user):
    return jsonify({
        "status": "Servicio de Inteligencia Online",
        "active_analyst": current_user,
        "port": PORT,
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/api/v1/analyze/hash', methods=['POST'])
@token_required
def analyze_hash(current_user):
    body = request.get_json()
    file_hash = body.get('hash')

    if not file_hash:
        return jsonify({"error": "Se requiere un hash para el tratamiento de datos"}), 400

    # Orquestación con API Externa (VirusTotal)
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": VT_API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            stats = data['data']['attributes']['last_analysis_stats']
            
            # Tratamiento de datos y lógica de riesgo
            malicious = stats['malicious']
            verdict = "LIMPIO" if malicious == 0 else "AMENAZA DETECTADA"
            
            return jsonify({
                "analyst": current_user,
                "hash": file_hash,
                "detections": malicious,
                "verdict": verdict,
                "risk_score": f"{malicious}/{sum(stats.values())}",
                "processed_at": datetime.datetime.now().isoformat()
            })
        
        return jsonify({"message": "Recurso no encontrado en VT"}), 404

    except Exception as e:
        return jsonify({"error": "Fallo en la conexión externa"}), 500

if __name__ == '__main__':
    print(f"Iniciando API de Ciberseguridad en el puerto {PORT}...")
    app.run(host='0.0.0.0', port=PORT, debug=True)