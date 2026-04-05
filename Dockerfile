 
FROM python:3.10-slim

# set working directory inside container
WORKDIR /app

# copy requirements first (for Docker layer caching)
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of the code
COPY . .

# expose port 5000
EXPOSE 5000

# run the app
CMD ["python", "app.py"]