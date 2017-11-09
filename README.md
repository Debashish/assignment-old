#Dependencies to be installed

sudo apt-get install mysql-server mysql-client
sudo apt-get install python-dev libmysqlclient-dev
sudo pip install MySQL-python
sudo pip install requests
sudo pip install Flask
sudo pip install Werkzeug

Run setup_schema.py to set up table schema

#Below are the curl requests to test the API's

List all team members - Request:

curl -X GET -H "Content-Type:application/json" http://localhost:5000/teammembers

Add a team member - Request:

curl -X POST -H "Content-Type:application/json" http://localhost:5000/team/member -d '{"member": {"phone_no": "1234567890", "email": "abcd@gmail.com", "first_name": "Test", "last_name": "Last", "role": "regular"}}'

Modify a team member - Request:

http://localhost:5000/team/member/<memberid>

Replace memberid with id of the team member to be modified

curl -X PUT -H "Content-Type:application/json" http://localhost:5000/team/member/3F4KEM -d '{"member": {"phone_no": "1234567890", "email": "test@gmail.com", "first_name": "Allen", "last_name": "Dar", "role": "regular"}}'

Delete a team member - Request:

http://localhost:5000/team/member/<memberid>

Replace memberid with id of the team member to be modified

curl -X DELETE -H "Content-Type:application/json" http://localhost:5000/team/member/3F4KEM -d '{"member": {}}'