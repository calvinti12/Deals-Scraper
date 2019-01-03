from github import Github

# First create a Github instance:

# using username and password
g = Github("anupkumarpanwar", "Sdtbtwtbtitbtewbsap@1511")


repo = g.get_repo("anupkumarpanwar/testing")

try:
	contents = repo.get_contents("test/test.txt", ref="master")
	repo.delete_file(contents.path, "remove test", contents.sha, branch="master")
except:
	pass




repo.create_file("test/test.txt", "testing", "test", branch="master")

# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)