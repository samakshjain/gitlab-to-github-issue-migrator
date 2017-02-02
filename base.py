from __future__ import print_function
import os

import gitlab
from github import Github

# Github creds
gh_token = os.environ.get('GITHUB_ACCESS_TOKEN') \
    or raw_input('Your Github email/username:  ')
# Gitlab creds
gl_token = os.environ.get('GITLAB_ACCESS_TOKEN') \
    or raw_input('Your GitLab email/username:  ')

gh = Github(gh_token)
gl = gitlab.Gitlab('https://gitlab.com', gl_token)


# list all the projects
# projects = gl.projects.list()
# for project in projects:
#     print(project)

# Check auth
gh_user = gh.get_user()
if gh_user:
    print('Github Authentication Successfull!')


def wizard():
    gl_repo_name = raw_input(
        'GitLab Project Name(Format: <team-name>/<project-name>):  '
    )

    gl_project = gl.projects.get(gl_repo_name)
    # Open issues
    gl_project_issues = gl_project.issues.list()

    if not gl_project_issues:
        print('You have issues, this project definetly doesn\'t')
        return

    gh_repo_name = raw_input('Github Repo Name:  ')
    gh_repo = gh_user.get_repo(gh_repo_name)

    if not gh_repo:
        print('Cannot find the github repo.')

    for issue in gl_project_issues:
        gh_repo.create_issue(
            issue.title,
            body=issue.description
        )

    print("Issues in Github Repo(" + gh_repo.name + "): \n\n")
    for issue in gh_repo.get_issues():
        print(issue.title)

    while True:
        q = raw_input("Continue? (y/n):  ")
        if q == 'y':
            return True
        elif q == 'n':
            return False


while True:
    if not wizard():
        break
