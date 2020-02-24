# Report Viewer Quick Start

Simple application shows the test logs.

## Clone the repo

    git clone https://github.com/liangxiao1/report_viewer.git

## Swith to repo directory and install required pkgs

    cd report_viewer
    pip install -r requirements.txt

## Create an Admin user(only required at first run)

    flask fab create-admin

## Start the app

    flask run -h 0.0.0.0 -p 5000

## Access it via below link

    http://$ip:5000

## References

### - *[Flask-AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/index.html)*



# Report Viewer in Container

Download app

```
cd /home/cheshi/containers/report_viewer/
git clone https://github.com/SCHEN2015/report_viewer.git
```

Start container

```
podman run --name report_viewer \
-v /home/cheshi/containers/report_viewer/:/data/:rw \
-p 5000:5000 -it fedora:31 /bin/bash
```

Install flaskapp

```
dnf install -y python3-flask python3-pip
pip3 install flask_appbuilder
```

Create an Admin user

```
cd /data/report_viewer
flask-3 fab create-admin
```

Run flaskapp instance

```
cd /data/report_viewer
flask-3 run -h 0.0.0.0 -p 5000
```

