FROM pypy:2-onbuild

RUN mkdir -p /opt/app

WORKDIR /opt/app

COPY . /opt/app

EXPOSE 5000
RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash" , "run.sh"]