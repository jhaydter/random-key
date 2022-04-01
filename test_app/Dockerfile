FROM python:3

WORKDIR /usr/src/app

### Build Flask app
COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# default port provided to random-key.py
ENTRYPOINT ["python", "random-key.py"]
CMD ["1234"]