FROM ubi8/ubi-minimal 

MAINTAINER "Rob Mokkink <rob@mokkinksystems.com"

RUN microdnf update -y && \
    microdnf install -y python3-pip && \
    microdnf clean all

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "/app/api.py"]
