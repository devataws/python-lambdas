# python-lambdas

Estimados, el desafío ha sido resuelto con tecnología serverless de AWS, especificamente con los servicios de API Gateway, AWS Lambda y DynamoDB.

Las funciones son escritas en lenguaje Python version 3.9 

Para utilizar el servicio REST por favor seguir las siguientes instrucciones:

Endpoint para Listar todos los usuarios:

https://dn7mg69be0.execute-api.us-east-1.amazonaws.com/users

Endpoint para Listar usuarios por id 

https://dn7mg69be0.execute-api.us-east-1.amazonaws.com/users/userid?id=0936f9e8-af1f-11ec-821a-9faea91aa602 

Si las pruebas las realizan por Postman, deben utilizar el verbo GET y pasar el parámetro id como Query Params y el valor del ID que quieren probar.

Endpoint para crear usuarios 

https://8rvn115eb9.execute-api.us-east-1.amazonaws.com/v1/users

payload de ejemplo:

{
    "date_of_birth": "1993-10-12",
    "email": "adrian23456@gmail.com",
    "last_name": "tapia silva",
    "name": "adrian ok"
}


Endpoint para actualizar usuarios por id, se debe utilizar verbo PUT

https://8rvn115eb9.execute-api.us-east-1.amazonaws.com/v1/users

payload de ejemplo:

{
  "id": "0936f9e8-af1f-11ec-821a-9faea91aa602",
  "name": "adrian ok",
  "last_name": "tapiaa silva",
  "email": "adriasdn23456@gmail.com",
  "date_of_birth": "1994-10-12"
}

Endpoint para eliminar usuarios por id, se debe utilizar verbo DELETE

https://8rvn115eb9.execute-api.us-east-1.amazonaws.com/v1/users

{
  "id": "0936f9e8-af1f-11ec-821a-9faea91aa602"
}



