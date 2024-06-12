FROM python:3.11

COPY . .

RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["python", "lambda_function.py"]
