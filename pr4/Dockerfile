ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim
COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ['python', 'app.py']
