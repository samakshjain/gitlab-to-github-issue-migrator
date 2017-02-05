## GitLab to Github Issue Migrator

===

## Usage

1. Get access token for [Github](https://help.github.com/articles/creating-an-access-token-for-command-line-use/), and set the environment variable `GITHUB_ACCESS_TOKEN` to its value.
2. For Gitlab, go to Settings > Access Tokens, create one and grant is API access and set `GITLAB_ACCESS_TOKEN`.
3. Clone the repo and `cd` into it.
4. Make a virtualenv and install the requirements.
	```pip install -r requirements.txt``` 
5. Execute the file `base.py` using ```python base.py```, and follow the instructions.
6. Hope it works.

===

Be wise, issues will be duplicated if you run the script again.
Repo names can be suffixed with the organization name as such `<generic_startup_name>/<marginally-witty-repo-name>`.
