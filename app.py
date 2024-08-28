from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # This enables CORS for all routes

ONOS_URL = 'http://172.17.0.1:8181/onos/v1'  # Replace with your ONOS server URL
ONOS_USER = 'onos'  # Replace with your ONOS username
ONOS_PASSWORD = 'rocks'  # Replace with your ONOS password

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data
    data = {"message": "Hello from Python"}
    return jsonify(data)

@app.route('/api/action', methods=['POST'])
def perform_action():
    content = request.json
    # Process the request and send commands
    response = {"status": "Action performed", "data": content}
    return jsonify(response)

def get_onos_headers(method):
    """Return headers for ONOS requests."""
    if method == 'GET':
        return {
            'Accept': 'application/json'
        }
    elif method == 'POST':
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

def send_onos_request(endpoint, method='GET', data=None):
    """Send an HTTP request to the ONOS server."""
    url = f"{ONOS_URL}/{endpoint}"
    try:
        response = requests.request(
            method,
            url,
            headers=get_onos_headers(method),
            auth=(ONOS_USER, ONOS_PASSWORD),
            json=data
        )
        # response = requests.get(url, auth=(ONOS_USER, ONOS_PASSWORD))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}

@app.route('/api/onosswitches', methods=['GET'])
def get_onos_switches():
    """Get a list of switches from ONOS."""
    response = send_onos_request('devices')
    
    switches = sorted([devices["id"] for devices in response["devices"]])
    return jsonify(switches)
    # return jsonify(response["devices"]["id"])

if __name__ == '__main__':
    app.run(port=5000)
