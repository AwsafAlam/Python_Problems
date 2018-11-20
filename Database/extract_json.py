import pymysql.cursors
import json
from DBConnector import DBConnector

# Connect to the database
dbconnector = DBConnector('localhost','root','','gerrit_test')

inline_comments = dbconnector.inline_comments()
patch_details = dbconnector.patch_details()
patches = dbconnector.patches()
# people = dbconnector.people()
requests = dbconnector.requests()
request_details = dbconnector.request_detail()
review_comments = dbconnector.review_comments()
reviews = dbconnector.reviews()


def getInlineComments(patch_id, req_id):
	I = {}
	for comment in inline_comments:
			if comment["patchset_id"] == patch_id and comment["request_id"] == req_id:
					I[comment["file_name"]] = {
						'comment_id': comment["comment_id"],
						'in_reply_to': comment["in_reply_to"],
						'line_number': comment["line_number"],
						'author_id': comment["author_id"],
						'written_on': comment["written_on"],
						'status': comment["status"],
						'side': comment["side"],
						'message': comment["message"],
						'start_line': comment["start_line"],
						'end_line': comment["end_line"],
						'start_character': comment["start_character"],
						'end_character': comment["end_character"],
						'sentiment_score': comment["sentiment_score"]
					}
	return I

def getReviews(req_id):
	R = {}
	for review in reviews:
		if review["request_id"] == req_id:
			R[review["id"]] = {
				'people_id': review["people_id"],
				'verified': review["verified"],
				'reviewed': review["reviewed"],
				'build': review["build"]
			}

	return R

def getPatchDetails(patch_id , req_id):
	D = {}
	for patch_detail in patch_details:
		if patch_detail["request_id"] == req_id and patch_detail["patchset_id"] == patch_id:
			D[patch_detail["file_name"]] = {
				'change_type': patch_detail["change_type"],
				'insertions': patch_detail["insertions"],
				'deletions': patch_detail["deletions"]
			}
			print(D[patch_detail["file_name"]])
	return D

def getPatches(patch_id , req_id):
	p = {}
	for patch in patches:
		if patch["request_id"] == req_id:
			p[patch["patch_id"]] = {
				'revision':  patch["revision"],
				'patchset_number':  patch["patchset_number"],
				'comment_count':  patch["comment_count"],
				'subject':  patch["subject"],
				'message':  patch["message"],
				'checkout':  patch["checkout"],
				'author':  patch["author"],
				'committer':  patch["committer"],
				'created':  patch["created"],
				'committed':  patch["committed"],
				'patch_file_details': getPatchDetails(patch_id , req_id),
				'inline_comments': getInlineComments(patch_id , req_id),
				'reviews': getReviews(req_id)
			}
	return p


def MakeRequestDict(req_id):
	for request_detail in request_details:
		if request_detail["request_id"] == req_id:
			return {
				'change_id': request_detail["change_id"],
				'gerrit_id': request_detail["gerrit_id"],
				'project': request_detail["project"],
				'branch': request_detail["branch"],
				'subject': request_detail["subject"],
				'status': request_detail["status"],
				'created': request_detail["created"],
				'updated': request_detail["updated"],
				'insertions': request_detail["insertions"],
				'deletions': request_detail["deletions"],
				'owner': request_detail["owner"],
				'number_patches': request_detail["number_patches"],
				'curent_patch_id': request_detail["curent_patch_id"],
				'revisions': getPatches(request_detail["curent_patch_id"] , req_id)
			}
	return {}

finalJSON = {}
## Here we will be getting list of 12k dict, which will be converted into JSON Array

# finalJSON[1] = MakeRequestDict(1)

for request in requests:
	finalJSON[request["request_id"]] = MakeRequestDict(request["request_id"])
	
	if len(finalJSON[request["request_id"]]) == 0:
		finalJSON.pop(request["request_id"])


with open('data.json', 'w') as outfile:  
   json.dump(finalJSON, outfile)

# y = json.dumps(finalJSON)
# print(y)
# print(requests[0][0])


