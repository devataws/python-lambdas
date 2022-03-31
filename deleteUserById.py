import boto3
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('Users')
    id_user = table.scan(FilterExpression=Attr('id').eq(event['id']))
    
    if id_user['Items'] != []:
        response = table.delete_item(
            Key={
            'id': event['id']
            }
        )
        return {
                   'statusCode': 200,
                   'body': 'Usuario eliminado'
               }
    else:
        return {
                  'statusCode': 200,
                  'body': 'Usuario no encontrado'
               }
