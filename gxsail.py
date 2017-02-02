print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')

from bigml.api import BigML
api = BigML('gsingle', '032c02951f1e8cb26ca209389bd95cce962b986b')
#from github import Github
#g = Github("gsingle", "sailcool17")
#for repo in g.get_user().get_repos():
#    print (repo.name)
#    repo.edit(has_wiki=False)

#source = api.create_source('sail.csv')
#source = api.create_source('https://drive.google.com/file/d/0B5xO24E5gaj9eE9NdWgtaVI5MUk/view?usp=sharing')
source = api.create_source('https://raw.githubusercontent.com/gsingle/GXsaiL/b709b8e598f293db96b56c497e43d2eba40de3c7/sail.csv')

dataset = api.create_dataset(source)
model = api.create_model(dataset)
#prediction = api.create_prediction(model, \
#    {'sepal length': 5, 'sepal width': 2.5})

#print('')
#api.pprint(prediction)

source = api.get_source(source)
api.ok(source)

dataset = api.get_dataset(dataset)
api.ok(dataset)

model = api.get_model(model)
api.ok(model)

#cluster = api.create_cluster(dataset,{"name": "my cluster","k":8})
cluster = api.create_cluster(dataset,{"name": "my cluster","critical_value":1}) #default value is 5 for g-means


api.ok(cluster)

batch_centroid = api.create_batch_centroid(cluster, dataset, {"name": "my batch centroid", "all_fields": True, "header": True})
api.ok(batch_centroid)


api.download_batch_centroid(batch_centroid, filename='my_clusters.csv')
#api.download_batch_centroid(batch_centroid, filename='https://raw.githubusercontent.com/gsingle/GXsaiL/master/my_clusters.csv')

from git import Repo

repo_dir = 'GXsaiL'
repo = Repo(repo_dir)
file_list = [
    'gxsail.py',
    'my_clusters.csv'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()




print('')
print('')
print('***** Job Complete *****')
print('')









