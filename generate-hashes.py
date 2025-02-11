import hashlib
import json
import os

boiii_json = []
boiii_folder = "./boiii/"

def get_file_hash(file_path):
	sha1_hash = hashlib.sha1()
	with open(file_path, 'rb') as f:
		while chunk := f.read(8192):
			sha1_hash.update(chunk)
	return sha1_hash.hexdigest()

for dirpath, _, filenames in os.walk(boiii_folder):
	for filename in filenames:
		full_path = os.path.join(dirpath, filename)
		relative_path = os.path.relpath(full_path, boiii_folder).replace(os.sep, '/')
		boiii_json.append([ relative_path, os.path.getsize(full_path), get_file_hash(full_path).upper() ])

with open("boiii.json", "w") as json_file:
	json.dump(boiii_json, json_file, indent=4)
