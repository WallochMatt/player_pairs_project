FROM python:alpine3.17
WORKDIR /home/projects
COPY . .
CMD ["python3", "main.py"]