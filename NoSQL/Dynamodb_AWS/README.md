# Dynamodb Tutorial by SCE
## Structure of a typical AWS project
![image](https://user-images.githubusercontent.com/18486562/99199635-654a3e80-2755-11eb-8a14-b4c40e1746a0.png)

## Setup
1. AWS account

## LEts goo!
1. Login to [AWS console](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fnc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fhomepage&forceMobileApp=0&code_challenge=YtRGx5Jc2FFMhIymxNE1uYB_DL4QPllGaRL8N2Wx9a0&code_challenge_method=SHA-256)

### Setting up Dynamodb
1. Go to Dynamodb
![image](https://user-images.githubusercontent.com/18486562/99199713-020cdc00-2756-11eb-844a-48b42bad5a50.png)

2. Create a table
![image](https://user-images.githubusercontent.com/18486562/99199744-28327c00-2756-11eb-9d90-622ef44fbada.png)

3. We will create a `people` table with `name` as an ID for each person.
![image](https://user-images.githubusercontent.com/18486562/99199768-59ab4780-2756-11eb-8889-4d091695eebc.png)

![image](https://user-images.githubusercontent.com/18486562/99200006-c115c700-2757-11eb-96eb-934d21beb3db.png)

<br><br><br>

### Setting up permission:
You always need to give any aws service permission to change others aws services
![image](https://user-images.githubusercontent.com/18486562/99201121-4dc38380-275e-11eb-9350-fbe08c5be6a1.png)


![image](https://user-images.githubusercontent.com/18486562/99202736-fd9bef80-2764-11eb-91ec-1c77e25222ab.png)

1. 

![image](https://user-images.githubusercontent.com/18486562/99204160-9df41300-2769-11eb-9240-379004ad726b.png)

2.

![image](https://user-images.githubusercontent.com/18486562/99204355-3b4f4700-276a-11eb-9b43-249ddb7f7180.png)

3. Empty `tag` (step 3) and give a rolename (step 4)

4. Navigate to the new Role -> `add inline policy`

![image](https://user-images.githubusercontent.com/18486562/99204504-c16b8d80-276a-11eb-89d4-cf996dadf039.png)

5. Service: `Dynamodb` and Action: `All Dynamodb action`

![image](https://user-images.githubusercontent.com/18486562/99204617-18716280-276b-11eb-9cee-c234dcd4114a.png)

6. Resource: `allow edit any table in this account`
![image](https://user-images.githubusercontent.com/18486562/99204729-66866600-276b-11eb-9830-6b21424237c9.png)

<br><br><br>

### Setting up Lambda
![image](https://user-images.githubusercontent.com/18486562/99200050-00441800-2758-11eb-8f8c-90e79bfdc9d4.png)

1. Choose `Lambda`
![image](https://user-images.githubusercontent.com/18486562/99200079-223d9a80-2758-11eb-8669-be1577bdf7eb.png)

2. Create Function

![image](https://user-images.githubusercontent.com/18486562/99200113-48633a80-2758-11eb-804b-1d35db743893.png)

![image](https://user-images.githubusercontent.com/18486562/99204833-b2d1a600-276b-11eb-8b54-0f60e5a6cd87.png)

2. Add a trigger

![image](https://user-images.githubusercontent.com/18486562/99200328-81e87580-2759-11eb-8af2-73ba900ec43e.png)

![image](https://user-images.githubusercontent.com/18486562/99200367-beb46c80-2759-11eb-99bb-b2750f6a4098.png)

## Lets write them codes
In `index.js`:
```js
var AWS = require('aws-sdk');
var dynamo = new AWS.DynamoDB.DocumentClient();

/**
 * Provide an event that contains the following keys:
 *
 *   - operation: one of the operations in the switch statement below
 *   - tableName: required for operations that interact with DynamoDB
 *   - payload: a parameter to pass to the operation being performed
 */
exports.handler = function(event, context, callback) {
    console.log('Received event:', event);

    var operation = event.operation;

    if (event.tableName) {
        event.payload.TableName = event.tableName;
    }

    switch (operation) {
        case 'create':
            dynamo.put(event.payload, callback);
            break;
        case 'read':
            dynamo.get(event.payload, callback);
            break;
        case 'update':
            dynamo.update(event.payload, callback);
            break;
        case 'delete':
            dynamo.delete(event.payload, callback);
            break;
        case 'list':
            dynamo.scan(event.payload, callback);
            break;
        case 'echo':
            callback(null, "Success");
            break;
        case 'ping':
            callback(null, "pong");
            break;
        default:
            callback('Unknown operation: ${operation}');
    }
};
```
![image](https://user-images.githubusercontent.com/18486562/99205128-6e92d580-276c-11eb-8ca1-303c812f3b12.png)

## Done
You can call this api through your `API GateWay`

![image](https://user-images.githubusercontent.com/18486562/99205273-e95bf080-276c-11eb-8a9c-22c460680315.png)

<br> <br> <br>

# Test Cases
1. Create a new test

![image](https://user-images.githubusercontent.com/18486562/99205562-c0882b00-276d-11eb-8d1f-f7f3ea28470a.png)

![image](https://user-images.githubusercontent.com/18486562/99205490-8a4aab80-276d-11eb-8d12-5ff7db130674.png)

<br> <br> 

## Test for Create:
```json
{
  "tableName": "people",
  "operation": "create",
  "payload": {
      "Item": { 
          "name" : "bob",
          "age" : 23
      }
  }
}
```
![image](https://user-images.githubusercontent.com/18486562/99205756-502dd980-276e-11eb-8c6a-251333654734.png)

<br> <br> 

## Test for Read:
```json
{
  "tableName": "people",
  "operation": "read",
  "payload": {
      "Key": {
          "name" : "bob"
      }
  }
}
```
or
```json
{
  "tableName": "people",
  "operation": "list",
  "payload": {
      "Key": {}
  }
}
```
![image](https://user-images.githubusercontent.com/18486562/99206551-82d8d180-2770-11eb-8ac7-29d2ab5871f8.png)

<br> <br> 

## Test for Delete:
```json
{
  "tableName": "people",
  "operation": "delete",
  "payload": {
      "Key": {
          "name" : "bob"
      }
  }
}
```
![image](https://user-images.githubusercontent.com/18486562/99200006-c115c700-2757-11eb-96eb-934d21beb3db.png)