FROM python
RUN apt-get update -y
#RUN apt-get install --reinstall libpq-dev
RUN apt-get install python-dev-is-python3 -y
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask
RUN echo "flask ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN mkdir -p /home/flask/app/web
WORKDIR /home/flask/app/web
COPY requirements.txt /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R flask:flaskgroup /home/flask
USER flask
ENTRYPOINT ["/usr/local/bin/gunicorn", "--bind", ":8000", "app:app", "--reload", "--workers", "16"]