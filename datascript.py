import json

files = ["yelp_academic_dataset_business.json",
    		"yelp_academic_dataset_checkin.json",
    		"yelp_academic_dataset_review.json",
    		"yelp_academic_dataset_user.json"]

business = [json.loads(line) for line in open(files[0], "r", encoding = 'utf-8')]
reviews = [json.loads(line) for line in open(files[2], "r", encoding = 'utf-8')]

d = {}

for b in business:
    i = b['business_id']
    if b['categories'] and 'Restaurants' in b['categories']:
        d[i] = [b, [], 0]
for rev in reviews:
    i = rev['business_id']
    if i in d.keys():
        d[i][1].append(rev)
        d[i][2] += 1

with open('data.json', 'w') as fp:
    json.dump(d, fp)
