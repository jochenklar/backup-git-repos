import argparse
import logging
import os
import subprocess
import yaml

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser('Backup a list of git repositories and keep them up to date.')
    parser.add_argument('-c', '--config', default='/etc/backup-git-repos.conf',
                        help='config file [default: /etc/backup-git-repos.conf]')
    parser.add_argument('-v', '--verbosity', default=0, type=int, choices=[0, 1, 2],
                        help='log level [default: 0]')
    args = parser.parse_args()

    setup_logger(args.verbosity)

    with open(args.config) as f:
        config = yaml.load(f.read())

    for repo in config['repos']:
        source = config['base_url'] + repo
        target = os.path.join(config['base_path'], repo)

        if os.path.exists(target):
            git_remote_update_prune(target)
        else:
            git_clone_mirror(source, target)


def setup_logger(verbosity):
    log_level = [logging.ERROR, logging.INFO, logging.DEBUG][verbosity]
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(log_level)


def git_clone_mirror(source, target):
    args = ['git', 'clone', '--mirror', source, target]
    logger.info('Run `%s`' % ' '.join(args))
    p = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    logger.debug(p.stdout.decode().strip())


def git_remote_update_prune(target):
    args = ['git', 'remote', 'update', '--prune']
    logger.info('Run `%s` in %s' % (' '.join(args), target))
    p = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=target)
    logger.debug(p.stdout.decode().strip())


if __name__ == "__main__":
    main()
