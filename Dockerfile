FROM python:3
LABEL MAINTAINER="Mahdi Akbari Zarkesh | https://learn2implemnet.ir"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /src
WORKDIR /src

# Installing requirements
ADD AuthJwt/requirement.txt /src
RUN pip install -r requirement.txt

EXPOSE 8000

# Run Server on entry point
CMD ["bash","StartDevelop.sh"]
