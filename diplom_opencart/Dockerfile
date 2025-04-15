FROM python:3.12-slim
WORKDIR /diplom_opencart
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]
CMD ["-v"]
