


# from flask import Flask, request, redirect
# import requests

# app = Flask(__name__)

# servers = ['http://127.0.0.1:5000', 'http://127.0.0.1:5001']
# server_index = 0

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])

# def forward_request(path):
#     global server_index
#     server = servers[server_index]
    
#     print(f"Routing request for: {path} with method: {request.method} to server: {server}")
    
#     server_index = (server_index + 1) % len(servers) 
    
#     if request.method == 'GET':
#         response = requests.get(f'{server}/{path}', params=request.args, allow_redirects=True)
#     elif request.method == 'POST':
#         response = requests.post(f'{server}/{path}', data=request.form)
#     elif request.method == 'PUT':
#         response = requests.put(f'{server}/{path}', data=request.form)
#     elif request.method == 'DELETE':
#         response = requests.delete(f'{server}/{path}', data=request.form)
    
#     return response.text, response.status_code


# if __name__ == '__main__':
#     app.run(debug=True, port=5003)
