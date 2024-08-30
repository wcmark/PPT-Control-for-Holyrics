import tkinter as tk
from tkinter import scrolledtext, messagebox
from flask import Flask, render_template, request, jsonify, send_from_directory, send_file
import requests, os, json

# Crear la aplicación Flask
app = Flask(__name__)

# Leer configuración inicial desde config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

ip = config.get('ip')
token = config.get('token')
puerto = config.get('puerto')

# Leer IP desde config.txt
with open('_internal/config.txt', 'r') as config_txt:
    ipWEB = config_txt.read().strip()

# Función para actualizar la configuración
def update_config():
    global ip, token, puerto, ipWEB
    ip = entry_ip.get()
    token = entry_token.get()
    puerto = entry_puerto.get()
    ipWEB = entry_ipWEB.get()

    # Guardar los valores en config.json
    with open('config.json', 'w') as config_file:
        json.dump({"ip": ip, "token": token, "puerto": puerto}, config_file, indent=4)

    # Guardar el valor de ipWEB en config.txt
    with open('_internal/config.txt', 'w') as config_txt:
        config_txt.write(ipWEB)

    messagebox.showinfo("Información", "Configuración actualizada correctamente")

# Configurar la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Configuración del Servidor")
root.resizable(False, False)


# Campos para config.json
tk.Label(root, text="IP del servidor:").grid(row=0, column=0, padx=10, pady=10)
entry_ip = tk.Entry(root)
entry_ip.grid(row=0, column=1, padx=10, pady=10)
entry_ip.insert(0, ip)

tk.Label(root, text="Token (API Holyrics):").grid(row=1, column=0, padx=10, pady=10)
entry_token = tk.Entry(root, show="*")
entry_token.grid(row=1, column=1, padx=10, pady=10)
entry_token.insert(0, token)

tk.Label(root, text="Puerto (API Holyrics):").grid(row=2, column=0, padx=10, pady=10)
entry_puerto = tk.Entry(root)
entry_puerto.grid(row=2, column=1, padx=10, pady=10)
entry_puerto.insert(0, puerto)

# Campo para config.txt
tk.Label(root, text="IP de transmisión web de Holyrics:").grid(row=3, column=0, padx=10, pady=10)
entry_ipWEB = tk.Entry(root)
entry_ipWEB.grid(row=3, column=1, padx=10, pady=10)
entry_ipWEB.insert(0, ipWEB)

# Botón para guardar configuración
btn_save = tk.Button(root, text="Guardar Configuración", command=update_config)
btn_save.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Campo de texto grande para mensajes/errores
txt_logs = scrolledtext.ScrolledText(root, width=40, height=10)
txt_logs.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


def log_message(message):
    txt_logs.insert(tk.END, message + '\n')
    txt_logs.see(tk.END)

# Ejemplo de cómo agregar un mensaje de log
log_message("Servidor en ejecución...")

# Integrar Flask con Tkinter
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config.txt')
def config():
    return send_file('config.txt')

@app.route('/<path:path>')
def serve_static(path):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), path)


@app.route('/actionNext', methods=['POST'])
def actionNext():
    client_ip = request.remote_addr
    url = f'http://{ip}:{puerto}/api/ActionNext?token={token}'
    headers = {'Content-Type': 'application/json'}
    data = {}

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            log_message(f"Acción siguiente ejecutada correctamente por {client_ip}")
            return jsonify(response.json())
        else:
            log_message(f"Error al realizar la solicitud desde {client_ip}: {response.status_code}")
            return jsonify({'error': 'Error al realizar la solicitud', 'status_code': response.status_code, 'text': response.text})
    except Exception as e:
        log_message(f"Error desde {client_ip}: {str(e)}")
        return jsonify({'error': 'Error de conexión', 'text': str(e)})


@app.route('/actionPrevious', methods=['POST'])
def actionPrevious():
    client_ip = request.remote_addr
    url = f'http://{ip}:{puerto}/api/ActionPrevious?token={token}'
    headers = {'Content-Type': 'application/json'}
    data = {}

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            log_message(f"Acción anterior ejecutada correctamente por {client_ip}")
            return jsonify(response.json())
        else:
            log_message(f"Error al realizar la solicitud desde {client_ip}: {response.status_code}")
            return jsonify({'error': 'Error al realizar la solicitud', 'status_code': response.status_code, 'text': response.text})
    except Exception as e:
        log_message(f"Error desde {client_ip}: {str(e)}")
        return jsonify({'error': 'Error de conexión', 'text': str(e)})

    
if __name__ == '__main__':
    # Ejecutar la interfaz gráfica en un hilo separado
    import threading
    flask_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=7000, debug=False))
    flask_thread.start()

    # Iniciar la aplicación Tkinter
    root.mainloop()
