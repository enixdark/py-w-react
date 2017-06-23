FROM node:6


MAINTAINER quandc <cqshinn92@gmail.com>

ENV HOME /root

ADD . /otp/app
WORKDIR /otp/app
RUN npm install
EXPOSE 3000
CMD npm start
