from github import Github
import getpass

username = input("Github username: ")
password = getpass.getpass("Github password: ")

github = Github(username, password)

# Then play with your Github objects:
for repo in github.get_user().get_repos():
    print(repo.name)

organization = github.get_user().get_orgs()[0]

print(organization)

repository_name = input("Github repository: ")
repository = organization.get_repo(repository_name)

sha = get_sha_for_tag(repository, 'master')

directory_to_download = input("Directory to download: ")
directory = download_directory(repository, sha, directory_to_download)

print(directory)