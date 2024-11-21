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
