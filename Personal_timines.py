import random
import time
import sys
from datetime import datetime
import os

def simulate_typing(text, min_delay=0.02, max_delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
    print()

def generate_log_entry():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    processes = ["data_pipeline", "ETL_job", "model_training", "data_validation", "db_connection"]
    messages = [
        f"Processed {random.randint(10000, 1000000)} rows in {random.uniform(0.5, 10.0):.2f} seconds",
        f"Data quality check: {random.randint(95, 100)}% of records passed validation",
        f"Database query completed in {random.uniform(0.1, 5.0):.2f}s",
        f"Model accuracy: {random.uniform(0.8, 0.99):.4f}",
        f"Data ingestion rate: {random.randint(1000, 10000)} records/second",
        f"Memory usage for data processing: {random.randint(50, 95)}%",
        f"Spark job completed with {random.randint(1, 10)} executors",
        f"API rate limit: {random.randint(80, 99)}% utilized",
        f"Data backup size: {random.randint(1, 1000)}GB",
        f"Cache hit ratio for analytics queries: {random.randint(70, 99)}%"
    ]
    return f"{current_time} [{random.choice(log_levels)}] {random.choice(processes)}: {random.choice(messages)}"

def create_fake_log_file(filename, num_entries=100):
    with open(filename, 'w') as f:
        for _ in range(num_entries):
            f.write(generate_log_entry() + '\n')

def simulate_log_monitoring():
    log_file = "data_pipeline.log"
    if not os.path.exists(log_file):
        create_fake_log_file(log_file)
    
    with open(log_file, 'r') as f:
        lines = f.readlines()
    
    start_line = random.randint(0, max(0, len(lines) - 20))
    for line in lines[start_line:start_line+10]:
        simulate_typing(line.strip())
        time.sleep(random.uniform(0.5, 1.5))

def run_data_command():
    commands = [
        ("python data_pipeline.py", [
            "Starting data pipeline...",
            "Connecting to data source...",
            "Extracting data...",
            "Transforming data...",
            "Loading data into data warehouse...",
            f"Pipeline completed. Processed {random.randint(10000, 1000000)} records in {random.uniform(10, 300):.2f} seconds."
        ]),
        ("spark-submit --class DataAnalysis data_job.jar", [
            "Initializing Spark session...",
            f"Reading {random.randint(1, 100)}GB of data from HDFS...",
            "Performing data aggregations...",
            "Running machine learning model...",
            f"Job completed. Execution time: {random.uniform(60, 600):.2f} seconds."
        ]),
        ("jupyter notebook", [
            "Initiating Jupyter Notebook...",
            "Starting Jupyter Notebook... ",
            "The Jupyter Notebook is running at:",
            "http://localhost:8888/?token=abcdef123456789",
            "Press Ctrl-C to stop this server and shut down all kernels"
        ]),
        ("docker run -d data-analysis-container", [
            f"Container ID: {os.urandom(32).hex()}",
            "Starting data analysis environment...",
            "Mounting data volumes...",
            "Initializing database connections...",
            "Container started successfully."
        ])
    ]
    
    command, output = random.choice(commands)
    simulate_typing(f"$ {command}")
    time.sleep(random.uniform(0.5, 1.5))
    for line in output:
        simulate_typing(line)
        time.sleep(random.uniform(0.1, 0.3))

def run_mock_terminal():
    while True:
        actions = [simulate_log_monitoring, run_data_command]
        random.choice(actions)()
        time.sleep(random.uniform(2, 5))

if __name__ == "__main__":
    try:
        simulate_typing("Initializing data analysis environment...")
        run_mock_terminal()
    except KeyboardInterrupt:
        simulate_typing("\nShutting down data analysis environment...")
    finally:
        if os.path.exists("data_pipeline.log"):
            os.remove("data_pipeline.log")
        simulate_typing("Cleaned up temporary files.")