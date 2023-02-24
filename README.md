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
### How to run project:
1. Clone the repository
2. Run following commands in cmd
```bash
virtualenv env
env/Scripts/activate
pip install -r requirements.txt
cd Nsn_assignment
python manage.py runserver
```
3. Now the backend is up and running in http://127.0.0.1:8000/