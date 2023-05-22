
import flask
from translateAzure import translateAzure
from translateAWS import translateAWS
from flask_cors import CORS
app = flask.Flask(__name__)

CORS(app)



@app.route("/api/translate", methods=["POST"])
def translate():
    # data=flask.request.data
    # print("data")
    # print(data)
    datajson=flask.request.json
    print("datajson")
    print(datajson)
    fromLang = datajson['from']
    toLang= datajson['to']
    text =datajson['inputText']

    response =  translateAzure.translateWithAzure(fromLang,toLang,text) 
   #check if Azure service respose is okay , if not translation service from AWS
    if(response.status_code==200):
        response = response.json()
        print("from Azure")
        print(response[0])
        translations = response[0]['translations']
        print(translations[0])

        return flask.jsonify(translations[0])
    else :
        response= translateAWS.translateWithAWS(fromLang,toLang,text)
        print(response)
        print("from AWS")
        translations = response['text']
        return flask.jsonify(response)
            

  

if __name__ == "__main__":
    print(("* Loading Flask starting server...port 5002"))
    app.run(host= '0.0.0.0', port=5002)