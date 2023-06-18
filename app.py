from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_pong():

    # Check if the request method is GET
    if request.method == 'GET':

        # Check if the request body is JSON
        if request.is_json:

            data = request.get_json()
            # Check if the JSON contains 'content' key and its value is 'ping'
            if 'content' in data and data['content'] == 'ping':
                response = {'message': 'pong'}
                # Return the response JSON with a status code of 200
                return jsonify(response), 200
            
            # Return an error response with status code 400 for invalid request body
        return jsonify({'error': 'Invalid request body'}), 400
    
    # Return an error response with status code 405 for other request methods
    else:

        return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    # Run the PingPong app on port 5005
    app.run(host='0.0.0.0' , port=5005)