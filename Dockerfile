FROM python:3
LABEL MAINTAINER="Mahdi Akbari Zarkesh | https://learn2implemnet.ir"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /src
WORKDIR /src

# Installing requirements
ADD AuthJwt/requirements.txt /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Run Server on entry point
CMD ["bash","StartDevelop.sh"]