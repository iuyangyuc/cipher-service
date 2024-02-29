FROM python:3.11-alpine
WORKDIR /home/application
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
COPY ./requirement.txt .
RUN pip install -r requirement.txt
COPY ./ciphers_project ciphers_project/
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]