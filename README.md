# Nsn-co

* Endpoint to view all the works: http://127.0.0.1:8000/api/works/
* Endpoint to view all the works filtered based on the work_type: http://127.0.0.1:8000/api/works/?work_type=['work_type']/
* Endpoint to view all the works filtered based on the artist: http://127.0.0.1:8000/api/works/?artist=['artist_name']/
* Endpoint to register new user: http://127.0.0.1:8000/api/register/
### Request format for registering user:
```javascript
{
  'username':'example123',
  'password':'example@12'
}

```
