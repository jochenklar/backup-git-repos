
---

🚫 **Discontinued.** This repository is no longer actively maintained.

---

backup-git-repos
================

Backup a list of git repositories and keep them up to date. This is done using:

```
git clone --mirror <repo>
```

and a subsequent use of

```
git remote update --prune
```

Setup
-----

Install using `pip`:

```
pip install git+https://github.com/jochenklar/backup-git-repos
```

Create a config file in `/etc/backup-git-repos.conf`:

```
base_url: 'git@github.com:'
base_path: /path/on/the/local/system/
repos:
- <github user>/<repo>
- <github user>/<repo>
- <github user>/<repo>

- <github orga>/<repo>
```

Usage
-----

```
usage: backup-git-repos [-h] [-c CONFIG] [-v {0,1,2}]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        config file [default: /etc/backup-git-repos.conf]
  -v {0,1,2}, --verbosity {0,1,2}
                        log level [default: 0]
```
