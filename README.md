# To Do List API 

Here we provide documentation for the TO Do List API : [View Here](https://todolist-api-django.vercel.com)

## Common Response Structure

#### status key

Every response contains a `status` key. This key represents the status of the API Request. Status can be one of the following values.

| Value | Description |
| --- | --- |
| `success` | The request is proccessed successfully and the desired outcome is got |
| `error` | An error is occured in proccessing the request. Like invalide request parameters, Authentication etc. |
| `internal-error` | This error is caused in rare condintion which is caused by the server itself. like Database connection errors etc. |

### data or message keys

The second response key would be either a `data` or `message`. Data or message is passed in the following scenariors.

- Data is passed when the response contains some type of data, either details of error or details of the result. Data will be always a json/dictionary containg values corresponding to the result.
- Message is passed when there is no data is available for the response. The response only contains a message which can represent either error or result. Message will be always a string or text.
    

### Response Example

``` json
{
  "status":"success",
  "data":{
    "key":"value",
  }
}

 ```

### Error Response

An Error response have the following structure

- Contains either a data or message
- In case of `message` there will be only a string message. ( `internal-error`will always return a message )
- In case of `data` there will be a object passed, containing which field has caused the error or something
    

##### Eg :

``` json
{
  "status":"error",
  "data":{
    "field_one":"This field is required",
    "field_two":"This field want to be a date"
  }
}

 ```

## Authorization

For authorization we use JWT Bearer token. This token is embedded in the Header of the request