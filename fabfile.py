from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/Mori-Dd/blog.git"

env.user = 'root'
env.password = 'LGH593949lgh'

env.hosts = ['morissf.com']

env.port = '22'


def deploy():
    source_folder = '/home/morissf/sites/morissf.com/blog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-morissf.com')
    sudo('service nginx reload')
