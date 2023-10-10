# To Do List API 

## Routes

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
  'username':'myuser',
  'password':'mypassword'
}
```

#### Response Structure

##### Success

```json
{
   'token':'agjisna5twywyu....'
}
```
 
##### Invalid Credentials
 
```json
{
  'message':'Invalid credentials!'
}
```
 