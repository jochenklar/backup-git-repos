import re

from setuptools import setup, find_packages

# get metadata from mudule using a regexp
with open('backup_git_repos/__init__.py') as f:
    metadata = dict(re.findall(r'__(.*)__ = [\']([^\']*)[\']', f.read()))

setup(
    name=metadata['title'],
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    maintainer=metadata['author'],
    maintainer_email=metadata['email'],
    license=metadata['license'],
    url='https://github.com/jochenklar/backup-git-repos',
    description=u'Backup a list of git repositories and keep them up to date using one binary.',
    long_description=open('README.md').read(),
    install_requires=[
        'PyYAML>=3.13',
        'GitPython>=2.1.11'
    ],
    classifiers=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'backup-git-repos=backup_git_repos.main:main'
        ]
    }
)
