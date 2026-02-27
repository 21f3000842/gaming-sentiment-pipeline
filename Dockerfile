# Start with a lightweight Python base
FROM python:3.11-slim

#2 Set the folder inside the container where our code will live
WORKDIR /app

#3 Copy the requirements list and install them
# We do this so that Docker caches the install (makes future builds faster)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#4 Copy the rest of the code into the container
COPY . .    

#5 Open the port than FastAPI uses
EXPOSE 8000

#6 The command to start the API
# We use --host 0.0.0.0 so that the container can talk to the computer
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]