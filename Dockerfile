<<<<<<< HEAD
FROM public.ecr.aws/lambda/python:3.10
=======
FROM public.ecr.aws/lambda/python:3.11
>>>>>>> 5356cd6a6991b57cd1b5ba8bacb034238d80035a

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]