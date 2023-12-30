Python text translator from one language to another using Azure and AWS cognitive services.

The textTranslator microservice, is developed using Python. This microservice exposes a POST endpoint on port 5002, with the route set as "/api/translate". Similar to the previous microservice, Flask is used as the web application framework to handle the POST requests received from the frontend.
The POST request parameters for this microservice include:
"inputText": This parameter holds the number in word format that needs to be translated.
"From": This parameter holds the default value of English, indicating the source language.
"to": This parameter holds the value of the target language to which the input text should be translated.
The textTranslator microservice consists of two classes: "translateAzure" and "translateAWS". The first class contains a method to translate the input text to a specific language using the Azure cognitive resource, which has been created in my Azure account. The second class, translateAWS, has a method that accepts input text and utilizes the AWS Translate service to perform the translation to the specified language. The microservice uses the boto3 AWS SDK, which is for Python, to access the translation functionality. For authentication purposes, my AWS access key and secret key, generated using the AWS IAM service, are utilized. The implementation includes a logic that if the request to the Azure translator service fails due to account credit or credential issues, the translation request is then made using the AWS service as a fallback option.
