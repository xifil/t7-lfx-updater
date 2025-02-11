import hashlib
import json
import os

boiii_json = []

def get_file_hash(file_path):
	sha1_hash = hashlib.sha1()
	with open(file_path, 'rb') as f:
		while chunk := f.read(8192):
			sha1_hash.update(chunk)
	return sha1_hash.hexdigest()

for dirpath, _, filenames in os.walk("."):
	for filename in filenames:
		full_path = os.path.join(dirpath, filename)
		relative_path = os.path.relpath(full_path, ".").replace(os.sep, '/')
		if relative_path.endswith(".py") and not "/" in relative_path:
			continue
		if relative_path.startswith(".git"):
			continue
		if relative_path == "boiii.json":
			continue
		boiii_json.append([ relative_path, os.path.getsize(full_path), get_file_hash(full_path).upper() ])

with open("boiii.json", "w") as json_file:
	json.dump(boiii_json, json_file, indent=4)
