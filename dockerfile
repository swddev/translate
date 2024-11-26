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

# Create env file for OPENAI_API_KEY
RUN echo "OPENAI_API_KEY=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" > .env


# Run the application
CMD ["uvicorn", "app.app:app", "--host=0.0.0.0", "--reload"]
