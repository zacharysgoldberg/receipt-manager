FROM python:3.9

# RUN apt-get update && apt-get upgrade -y

# EXPOSE 80
# EXPOSE 443
EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app", "-w", "2", "-k", "uvicorn.workers.UvicornWorker"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

