from flask import Flask, request, jsonify
from Services.search_service import SearchService
from Services.gig_service import GigService
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
port = int(os.getenv("PORT",10000))


@app.route('/search', methods=['POST'])
def perform_search():

    try:
        data = request.get_json()
        searchSercvice = SearchService()
        results = searchSercvice.semanticSearch(data['query'], data['count'])
        gigService = GigService()
        gig_dtos = gigService.extract_results(results)
        formatted_results = gigService.get_results_as_dict()

        return jsonify(formatted_results), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
    # serve(app, host='0.0.0.0', port=5000)
