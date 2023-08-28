from utils.env_vars import *
from utils import summarization
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Summarization API'

@app.route('/api', methods=['GET','POST'])
def process_request():
    data = request.json
    
    file_url = data.get("file_url", "")
    mode = data.get("mode", "")
    
    if mode == 'refine':
        summary = summarization.summarize_document(file_url, mode=mode, verbose = True)
        response_text = summary['summary']
    else:
        response_text = "Mode not supported."
    return response_text

# from utils import summarization_no_fr

# @app.route('/api', methods=['GET','POST'])
# def process_request():
#     data = request.json
    
#     file_text = data.get("file_text", "")
#     mode = data.get("mode", "")
    
#     if mode == 'refine':
#         summary = summarization_no_fr.summarize_document(file_text, mode=mode, verbose = True)
#         response_text = summary['summary']
#     else:
#         response_text = "Mode not supported."
#     return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)