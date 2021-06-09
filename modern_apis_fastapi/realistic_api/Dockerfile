FROM tiangolo/uvicorn-gunicorn-fastapi

RUN apt-get update -y

ARG WORKDIR=/opt/app
WORKDIR ${WORKDIR}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

# COPY .env .env
# COPY static static
# COPY templates templates
# COPY app app
# COPY wsgi.py wsgi.py