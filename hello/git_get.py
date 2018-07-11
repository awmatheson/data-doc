from github import Github
import getpass
import os
from github import GithubException
import base64

# username = input("Github username: ")
# password = getpass.getpass("Github password: ")

def get_sha_for_tag(repository, tag):
    """
    Returns a commit PyGithub object for the specified repository and tag.
    """
    branches = repository.get_branches()
    matched_branches = [match for match in branches if match.name == tag]
    if matched_branches:
        return matched_branches[0].commit.sha

    tags = repository.get_tags()
    matched_tags = [match for match in tags if match.name == tag]
    if not matched_tags:
        raise ValueError('No Tag or Branch exists with that name')
    return matched_tags[0].commit.sha

def download_directory(repository, sha, server_path):
    """
    Download all contents at server_path with commit tag sha in
    the repository.
    """
    contents = repository.get_dir_contents(server_path, ref=sha)

    DAGS = {}

    for content in contents:
        print "Processing %s" % content.path
        if content.type == 'dir':
            download_directory(repository, sha, content.path)
        else:
            try:
                path = content.path
                if 'dags' in path:
                	file_content = repository.get_contents(path, ref=sha)
                	file_data = base64.b64decode(file_content.content)
                	DAGS[content.name]=file_data
                # file_out = open(content.name, "w")
                # file_out.write(file_data)
                # file_out.close()
            except (GithubException, IOError) as exc:
                # logging.error('Error processing %s: %s', content.path, exc)
                print('Error processing %s: %s', content.path, exc)
    return DAGS

PASSWORD = os.getenv('GITPASS')

github = Github('awmatheson', PASSWORD)

# Then play with your Github objects:
for repo in github.get_user().get_repos():
    if repo.name == 'data-warehouse':
    	print([i for i in repo.get_keys()])
    	sha = get_sha_for_tag(repo, 'master')
    	dags = download_directory(repo, sha, 'python')
    	break

for key,value in dags:
	print(key)
	print(value[:100])
