import boto3

class translateAWS:
      def translateWithAWS(fromLang, toLang,text):
            aws_access_key_id = 'AKIAWUUKE34OPY3IQH2M'
            aws_secret_access_key = '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'
            region_name = 'us-east-1'  
            client = boto3.client('translate', aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                region_name=region_name)

            response = client.translate_text(
                Text=text,
                SourceLanguageCode=fromLang,
                TargetLanguageCode=toLang
            )

            translated_text = response['TranslatedText']

            responsedata={
                'text':translated_text,
                'to':toLang
            }

            print("responsedata")
            print(responsedata)
            return responsedata

 

      