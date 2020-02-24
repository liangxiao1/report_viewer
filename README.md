# Composite keys Example

Simple application showing the test logs.

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
dnf install -y python3-flask
pip3 install flask_appbuilder
```

Create an Admin user

```
flask-3 fab create-admin
```

Run flaskapp instance

```
flask-3 run -h 0.0.0.0 -p 5000
```
