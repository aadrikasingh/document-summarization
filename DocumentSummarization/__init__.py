import logging

import azure.functions as func

def get_param(req, param_name):
    param = req.params.get(param_name) 

    if not param:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            param = req_body.get(param_name)
    
    return param

from utils import summarization
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    file_url = get_param(req, 'file_url')
    mode = get_param(req, 'mode')

    if file_url:
        summary = summarization.summarize_document(file_url, mode=mode, verbose = True)
        answer = summary['summary']
        return func.HttpResponse(answer)
    
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

# from utils import summarization_no_fr
# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     file_text = get_param(req, 'file_text')
#     mode = get_param(req, 'mode')

#     if file_text:
#         summary = summarization_no_fr.summarize_document(file_text, mode=mode, verbose = True)
#         answer = summary['summary']
#         return func.HttpResponse(answer)
    
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )