from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('kerberos.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Determine if the request is from the GUI or an API
    if request.content_type == 'application/json':
        data = request.get_json()
        user_principal = data.get('user_principal')
        password = data.get('password')
    else:
        user_principal = request.form.get('user_principal')
        password = request.form.get('password')

    if not user_principal or not password:
        return jsonify({"status": "error", "message": "Missing user principal or password"}), 400

    try:
        # Run kinit with the provided credentials
        process = subprocess.run(
            ["kinit", user_principal],
            input=password.encode(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if process.returncode == 0:
            return jsonify({"status": "success", "message": "Authentication successful!"})
        else:
            return jsonify({"status": "error", "message": process.stderr.strip()}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/list_tickets', methods=['GET'])
def list_tickets():
    try:
        # Run klist to list Kerberos tickets
        process = subprocess.run(
            ["klist"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if process.returncode == 0:
            return jsonify({"status": "success", "tickets": process.stdout.strip()})
        else:
            return jsonify({"status": "error", "message": process.stderr.strip()}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
