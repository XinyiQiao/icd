FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# update, upgrade, and install packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y apt-utils \
    && apt-get install -y curl git less man nano sudo wget \
    && apt-get install -y build-essential

# configure apt-utils (fixes warnings)
RUN dpkg-reconfigure apt-utils

# set some useful defaults
RUN echo "alias ls='ls --color'" >> /etc/bash.bashrc
RUN echo "alias grep='grep --color=auto'" >> /etc/bash.bashrc

# download get-pip and install
RUN wget -P /tmp https://bootstrap.pypa.io/get-pip.py
RUN python /tmp/get-pip.py

# install ipython
RUN pip install ipython

WORKDIR /app

# install base requirements
COPY ./requirements /requirements
RUN pip install -r /requirements/base.txt

# copy entrypoint and make executable
COPY ./compose/icd/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy start script and make executable
COPY ./compose/icd/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

# copy and install package
COPY . /app
RUN pip install /app

ENTRYPOINT ["/entrypoint.sh"]
