FROM python:3.11.7-alpine3.19

LABEL Maintainer="CIMSA"
WORKDIR /code

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY ./app /code/app

# Set the environment variable for OpenAI API key (replace with your key or set it externally)
ENV OPENAI_API_KEY=<your_openai_api_key>


# Run the application
CMD ["uvicorn", "app.app:app", "--host=0.0.0.0", "--reload"]
