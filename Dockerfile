FROM python:3.7-slim
COPY . /wa-action
WORKDIR /wa-action
CMD ["python", "/wa-action/app.py"]
