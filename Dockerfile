FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "random-key.py"]
CMD ["1234"]