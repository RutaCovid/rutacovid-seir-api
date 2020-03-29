from flask import Flask, jsonify
from models import model_results

app = Flask(__name__)

@app.route('/api/seir', methods=['GET'])
def get_seir():
    return jsonify({'seir': model_results})

@app.route('/api/seir/<string:result>', methods=['GET'])
def get_result():
	model_result = [model_result for model_result in model_results if model_results['results'] == result]
	
	if len(model_result) == 0:
		abort(404)

	return jsonify({'result': model_result[0]})

# @app.route('/api/seir/susceptible', methods=['GET'])
# def get_susceptible():
# 	return jsonify({'susceptible':model_results["susceptible"]})

# @app.route('/api/seir/exposed', methods=['GET'])
# def get_exposed():
# 	return jsonify({'exposed':model_results["exposed"]})

# @app.route('/api/seir/infected', methods=['GET'])
# def get_infected():
# 	return jsonify({'infected':model_results["infected"]})

# @app.route('/api/seir/recovered', methods=['GET'])
# def get_recovered():
# 	return jsonify({'recovered':model_results["recovered"]})

if __name__ == '__main__':
    app.run(debug=True)