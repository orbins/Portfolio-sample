FROM python:3.9-alpine3.16

RUN mkdir -p /core/

COPY requirments.txt /core/requirments.txt

RUN pip install --no-cache-dir -r /core/requirments.txt

COPY main core/main/

WORKDIR core/main/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



