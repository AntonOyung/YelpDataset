import json

files = ["./yelp_academic_dataset_business.json",
    		"./yelp_academic_dataset_checkin.json",
    		"./yelp_academic_dataset_review.json",
    		"./yelp_academic_dataset_user.json"]

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
t0p3 = sorted([(key, value) for key, value in d.items()], key=lambda x: x[1][2], reverse=True)[:3]
# num_rev_dict = {}
# for business in d:
#     num_rev_dict[business] = d[0][business][2]
# sorted_num_rev_dict = sorted(num_rev_dict.items(), key = lambda x: x[1], reverse=True)
# temp = sorted_num_rev_dict
with open('top3.json', 'w') as fp:
    json.dump(t0p3, fp)
