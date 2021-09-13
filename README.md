# Wrapper GIT

Full wrapper of git command for handle multiple accounts and servers.

# Install

* Install from git+https:

```
pip install git+https://github.com/ericsonj/wgit
```

* Install from git:

```
git clone https://github.com/ericsonj/wgit
cd wgit
pip install .
```

# Add complete for your terminal

## **Bash**

Append the next line in file `~/.bashrc`:

```bash
_completion_loader git
eval $(complete -p git | perl -pe 's/(\s)git$/$1wgit/')
```

## **ZSH** https://ohmyz.sh/ 

Append the next line in file `~/.zshrc`:

```zsh
compdef wgit=git
```

## 🐟 **Fish Shell** https://fishshell.com/

Append the next line in file `~/.config/fish/config.fish`, create if not exist:

```
complete -c wgit -w git
```

# Configuration

wgit need the configuration file `~/.config/wgit/accounts.json`

```
wgit: 🚨 Accounts file not found, create the file ~/.config/wgit/accounts.json
wgit:    You can use the template https://github.com/ericsonj/wgit/blob/main/accounts.json
```

You have to configure in this file yours git accounts and SSH keys, example:

```json
[
    {
        "name": "gitlab",
        "author": "author",
        "email": "email",
        "host_owners": [
            "gitlab.*"
        ],
        "IdentityFile": "~/.ssh/id_rsa"
    },
    {
        "name": "github",
        "author": "author",
        "email": "email",
        "host_owners": [
            "github.*"
        ],
        "IdentityFile": "~/.ssh/id_rsa"
    }
]
```
## Options

* **name** [*string*]: account configuration name
* **author** [*string*]: author of git, is use for: GIT_AUTHOR_NAME, GIT_COMMITTER_NAME.
* **email** [*string*]: email of git, is use for: GIT_AUTHOR_EMAIL, GIT_COMMITTER_EMAIL.
* **IdentityFile** [*string*]: path of ssh-key.
* **host_owners** [*list*]: list of regex strings for search and identified the repository, ex: 'git@github.com:job/repo' -> github_job.
    + `"github.*"`: match any github repository. (Commons for personal account)
    + `"gitlab.*"`: match any gitlab repository. (Commons for personal account)
    + `"gitlab_job"`: match any gitlab repository with owner equal to 'job'. (Commons for job account or secondary account)
* **GIT_CONFIG** [*string*]: specific git config file by account.
* **GIT_EDITOR** [*string*]: is the editor Git will launch when the user needs to edit some text.
* **GIT_\*** [*string*]: set environment git variable, see https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables.

## Example account.json

```json
[
    {
        "name": "myjob_gitlab",
        "host_owners": [
            "gitlab_myjob",
            "gitlab_myjobgroup"
        ],
        "IdentityFile": "~/.ssh/id_myjob_gitlab",
        "GIT_CONFIG": "/home/ericson/.config/wgit/gitlab_myjob_config"
    },
    {
        "name": "gitlab",
        "host_owners": [
            "gitlab.*"
        ],
        "IdentityFile": "~/.ssh/id_rsa",
        "author": "Ericson Joseph",
        "email": "ericsonjoseph@gmail.com"
    },
    {
        "name": "github",
        "host_owners": [
            "github.*"
        ],
        "IdentityFile": "~/.ssh/id_rsa",
        "author": "Ericson Joseph",
        "email": "ericsonjoseph@gmail.com",
        "GIT_EDITOR": "vim"
    }
]
```
