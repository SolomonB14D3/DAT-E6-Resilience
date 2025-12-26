FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir torch pandas numpy seaborn scipy matplotlib
COPY . .
CMD ["bash", "manuscript/run_all_sims.sh"]