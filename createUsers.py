from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
import uuid, re   
import boto3

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
date_format = '%Y-%m-%d'

def lambda_handler(event, context):
    
    try:
        re.search(regex,event['email']) and datetime.strptime(event['date_of_birth'], date_format) 
        
        client = boto3.resource('dynamodb')
        table = client.Table('Users')
         
        r = table.scan(FilterExpression=Attr('email').eq(event['email']))
        
        if r['Items'] != []:
            return {
                'statusCode': 200,
                'body': 'E-mail registrado, intente con otro correo.' 
            }
            
        else:
            response = table.put_item(
                Item = {
                        'id': str(uuid.uuid1()),
                        'name': event['name'],
                        'last_name': event['last_name'],
                        'email': event['email'],
                        'date_of_birth': event['date_of_birth']
                    })
                    
            return {
                'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
                'body': 'Registro creado'
            }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': 'Bad request' 
        }
        
