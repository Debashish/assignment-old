from flask import Flask, Response, request
from flask import jsonify
import requests, json, time
import MySQLdb
import db_handle
import string
import random

app = Flask(__name__)


def checkAllFields(req_body):

	val = req_body['member'].values()

	if len(val) == 5:
		return True
	else:
		return False

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


@app.route('/teammembers')
def getAllMembers():

	results = db_handle.allMembers("team")
	lst = []
	for result in results:
		temp_dct = {}
		temp_dct['member_id'] = result[0]
		temp_dct['first_name'] = result[1]
		temp_dct['last_name'] = result[2]
		temp_dct['phone_no'] = result[3]
		temp_dct['email'] = result[4]
		temp_dct['role'] = result[5]
		lst.append(temp_dct)

	result_dct = {"members":lst}
	return jsonify(result_dct)

@app.route('/team/member', methods=['POST'])
def addTeamMember():

	req_body = request.get_json(force=True)
	print req_body

	bool_val = checkAllFields(req_body)

	if bool_val == False:

		error = {"Error": "One more fields are missing"}

		return jsonify(error)

	else:

		member_id = id_generator()
		first_name = req_body['member']['first_name']
		last_name = req_body['member']['last_name']
		email = req_body['member']['email']
		phone_no = req_body['member']['phone_no']
		role = req_body['member']['role']
		status = db_handle.insertToDb("team", member_id, first_name, last_name, phone_no, email, role)
		print status
		if status == 1:
			result_dct = {"member": {"member_id":member_id, "first_name":first_name, "last_name":last_name, "phone_no": phone_no, "email": email, "role": role}}
			return jsonify(result_dct)
		else:
			error = {"Error": "Internal server error"}
			return jsonify(error)

@app.route('/team/member/<member_id>', methods = ['PUT'])
def updateTeamMember(member_id):

	req_body = request.get_json(force=True)
	new_properties = req_body['member']

	if len(new_properties.values()) == 0:

		error = {"Error": "Fields cannot be empty"}

		return jsonify(error)

	else:
		status = db_handle.updateDb("team", member_id, new_properties)
		print status
		member = {"member_id":member_id}
		if status == 1:
			for key, val in new_properties.iteritems():
				member[key] = val
			result_dct = {"member": member}
			return jsonify(result_dct)
		else:
			error = {"Error": "The team member does not exist"}
			return jsonify(error)

@app.route('/team/member/<member_id>', methods = ['DELETE'])
def removeTeamMember(member_id):

	status = db_handle.deleteFromDb("team", member_id)
	if status == 1:
		result_dct = {"member": {}}
		return jsonify(result_dct)
	else:
		error = {"Error": "Internal server error"}
		return jsonify(error)




if __name__ == "__main__":

    app.debug = False
    app.run(host='localhost')





