from __future__ import with_statement

from StringIO import StringIO
from fabric.api import local, settings, abort, run, cd, env, get, warn_only, sudo
from fabric.contrib.files import exists

env.roledefs = {
    'dev': ['localhost'],
    'staging': ['staging.equitrack.uniceflebanon.org'],
    'production': ['equitrack.uniceflebanon.org']
}


def get_id_of_running_image(name):
    print('>>> Get current container id if exists')
    if exists(name):
        fd = StringIO()
        get(name, fd)
        return fd.getvalue()
    return None


def snapshot_container_to_image(container, image, tag):
    print('>>> Committing current container')
    run('docker commit {} {}:{}'.format(container, image, tag))


def build_image_with_packer(from_image, to_image, tag='latest', packer_file='packer.json'):
    print('>>> Building new image with file {}'.format(packer_file))
    with settings(sude_user='jcranwellward'):
        run("packer build -var 'from_image={from_image}' -var 'to_image={to_image}' -var 'tag={tag}' {file}".format(
            file=packer_file,
            from_image=from_image,
            to_image=to_image,
            tag=tag
        ))


def stop_container(container, name=''):
    print('>>> Stopping container {}'.format(container))
    run('docker stop {}'.format(container))
    if name:
        with warn_only():
            run('rm {}'.format(name))


def start_container(name, image, command, port, **envs):
    print('>>> Starting new container for image {}'.format(image))
    run(
        'docker run --name={name} --cidfile={name} -p {port} -d {envs} {image} {command}'.format(
        name=name, image=image, port=port, command=command, envs='-e '.join(
            ['"{}={}" '.format(key, value) for key, value in envs])
        )
    )


def remove_container(container):
    print('>>> Removing container {}'.format(container))
    run('docker rm -f {}'.format(container))


def docker_ps(all=True):
    run('docker ps {}'.format('-a' if all else ''))


def docker_images():
    return run('docker images')


def deploy(name, image, branch='develop', git_dir='/vagrant'):
    # pull new code from github
    with cd(git_dir):
        run("git pull origin {}".format(branch))
        current = get_id_of_running_image(name)
        if not current:
            build_image_with_packer(image, image)
        else:
            snapshot_container_to_image(current, image, 'latest')
            build_image_with_packer(image, image)
            snapshot_container_to_image(current, image, 'backup')
            stop_container(current, name)

        start_container(name, image, 'supervisord', '80')




