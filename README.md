# To Do List API 

Here we provide the API documentation for the To Do List.

## Common Response Structure

#### `status` key

Every response contains a `status` key. This key represents the status of the API Request. Status can be one of the following values.

| Value | Description |
| -- | -- |
| `success` | The request is proccessed successfully and the desired outcome is got |
| `error` | An error is occured in proccessing the request. Like invalide request parameters, Authentication etc. |
| `internal-error` | This error is caused in rare condintion which is caused by the server itself. like Database connection errors etc. |

### `data` or `message` keys

The second responce key would be either a `data` or `message`. Data or message is passed in the following scenariors.

- Data is passed when the responce contains some type of data, either details of error or details of the result. Data will be always a json/dictionary containg values corresponding to the result.
- Message is passed when there is no data is available for the responce. The responce only contains a message which can represent either error or result. Message will be always a string or text. 

## Access Routes 

### Access Token

> /auth/token/ [POST]

#### Request Structure

| Key | Value |
| -- | -- |
| username | &lt;Username of a registered user> |
| password | &lt;Password of the correspondung user> |

##### Example 

```json
{
  "username":"myuser",
  "password":"mypassword"
}
```

#### Response Structure

##### Success

```json
{
   "token":"agjisna5twywyu...."
}
```
 
##### Invalid Credentials
 
```json
{
  "message":"Invalid credentials!"
}
```
 
### User Registration

> /auth/register 

#### Request paraneters 

| Key | Value |
| -- | -- |
| first_name | First name |
| second_name | Second Name |
| email | Email id |
| username | Username |
| password | Password |

