import json


def lambda_handler(event, context):
    key_word = event['keyword']
    if key_word != "":
        return {
            'statusCode': 200,
            'body': json.dumps("Aparna Reddy Pothula says " + key_word)
        }
    else:
        return {
            'statusCode': 422,
            'body': json.dumps("Keyword is not been given")
        }