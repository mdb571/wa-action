FROM python:3.7-slim
COPY . /wa-action
WORKDIR /wa-action
RUN pip install --target=/wa-action requests
CMD ["python", "/wa-action/app.py"]
