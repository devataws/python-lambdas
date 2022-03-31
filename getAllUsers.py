import boto3

def lambda_handler(event, context):

   client = boto3.resource('dynamodb')
   table = client.Table('Users')
   
   try:
       response = table.scan()
       return response['Items']
   except Exception as e:
       return {
           'statusCode': 400,
            'body': 'Bad request'
       }
       
