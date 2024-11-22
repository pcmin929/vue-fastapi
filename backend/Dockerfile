FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy requirements file
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy application code
COPY . .

# Step 7: Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
