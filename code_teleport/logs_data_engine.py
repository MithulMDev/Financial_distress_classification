import random
import time
import sys
from datetime import datetime

def simulate_typing(text, min_delay=0.50, max_delay=1.25):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
    print()

# Pre-generate a large set of unique log entries
log_entries = [
    "[INFO] data_pipeline: Processed {rows} rows in {time:.2f} seconds",
    "[WARNING] ETL_job: Data quality check: {quality}% of records passed validation",
    "[ERROR] model_training: Training interrupted due to insufficient memory",
    "[DEBUG] data_validation: Detected {anomalies} anomalous data points",
    "[INFO] db_connection: Database query completed in {query_time:.2f}s",
    "[INFO] api_service: API rate limit: {rate_limit}% utilized",
    "[WARNING] batch_processing: Job completed with {errors} errors",
    "[INFO] data_ingestion: Ingested {data_size}GB from source systems",
    "[DEBUG] cache_manager: Cache hit ratio for analytics queries: {cache_hit}%",
    "[INFO] feature_engineering: Completed for {variables} variables",
    "[WARNING] data_drift: Detected {drift:.2f}% drift in target variable",
    "[INFO] anomaly_detection: Flagged {flagged} records for review",
    "[DEBUG] dashboard_update: Real-time dashboard updated with {datapoints} new data points",
    "[INFO] spark_job: Distributed processing completed on {nodes} nodes",
    "[WARNING] data_backup: Incremental backup size: {backup_size}GB",
    "[INFO] model_evaluation: Model accuracy improved by {improvement:.2f}%",
    "[DEBUG] data_transformation: Applied {transformations} unique transformations",
    "[WARNING] resource_monitor: GPU utilization peaked at {gpu_usage}%",
    "[INFO] data_archiving: Archived {archived} obsolete datasets",
    "[DEBUG] streaming_pipeline: Processed {events} events in real-time"
]

# Pre-generate a set of varied command outputs
command_outputs = [
    ("python data_pipeline.py --source cloud_storage --destination data_warehouse", [
        "Initializing data pipeline...",
        "Connecting to cloud storage...",
        "Extracting data: {progress}% complete",
        "Applying transformations: {progress}% complete",
        "Loading into data warehouse: {progress}% complete",
        "Pipeline completed. Processed {rows} records in {time:.2f} minutes."
    ]),
    ("spark-submit --class DataAnalysis job.jar", [
        "Initializing Spark session...",
        "Reading {size}GB of data from distributed storage...",
        "Performing data aggregations: {progress}% complete",
        "Running machine learning model: {progress}% complete",
        "Job completed. Execution time: {time:.2f} minutes."
    ]),
    ("kubectl get pods -n data-processing", [
        "NAME                                READY   STATUS    RESTARTS   AGE",
        "data-pipeline-{hash}      1/1     Running   0          {age}",
        "spark-worker-pool-{hash}   1/1     Running   0          {age}",
        "jupyter-notebook-{hash}   1/1     Running   0          {age}",
        "airflow-scheduler-{hash}   1/1     Running   0          {age}"
    ]),
    ("airflow dags list", [
        "dag_id                      | filepath                | owner   | paused",
        "=========================== | ======================= | ======= | ======",
        "daily_data_ingestion        | dags/data_ingestion.py  | airflow | False",
        "weekly_data_quality_check   | dags/data_quality.py    | airflow | False",
        "monthly_model_training      | dags/model_training.py  | airflow | False",
        "realtime_anomaly_detection  | dags/anomaly_detect.py  | airflow | False"
    ])
]

def generate_unique_log_entry():
    template = random.choice(log_entries)
    return template.format(
        rows=random.randint(10000, 1000000),
        time=random.uniform(0.5, 60.0),
        quality=random.randint(95, 100),
        anomalies=random.randint(1, 1000),
        query_time=random.uniform(0.1, 5.0),
        rate_limit=random.randint(80, 99),
        errors=random.randint(0, 100),
        data_size=random.randint(1, 1000),
        cache_hit=random.randint(70, 99),
        variables=random.randint(10, 100),
        drift=random.uniform(0.01, 1.0),
        flagged=random.randint(1, 1000),
        datapoints=random.randint(100, 10000),
        nodes=random.randint(5, 100),
        backup_size=random.randint(1, 1000),
        improvement=random.uniform(0.1, 5.0),
        transformations=random.randint(5, 50),
        gpu_usage=random.randint(80, 100),
        archived=random.randint(1, 100),
        events=random.randint(1000, 1000000)
    )

def generate_unique_command_output():
    command, output_template = random.choice(command_outputs)
    output = [line.format(
        progress=random.randint(0, 100),
        rows=random.randint(10000, 1000000),
        time=random.uniform(0.5, 60.0),
        size=random.randint(1, 1000),
        hash=f"{random.randint(100000, 999999):x}",
        age=f"{random.randint(1, 30)}d{random.randint(1, 23)}h"
    ) for line in output_template]
    return command, output

def run_simulation():
    start_time = datetime.now()
    while True:
        current_time = datetime.now()
        elapsed_time = current_time - start_time
        
        if random.random() < 0.7:  # 70% chance of log entry
            log_entry = generate_unique_log_entry()
            simulate_typing(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} {log_entry}")
        else:  # 30% chance of command output
            command, output = generate_unique_command_output()
            simulate_typing(f"$ {command}")
            for line in output:
                simulate_typing(line)
        
        # Display a system summary every 5 minutes
        if elapsed_time.seconds % 300 < 5:
            summary = f"""
System Summary (Elapsed Time: {elapsed_time}):
CPU Usage: {random.uniform(20, 80):.1f}%
Memory Usage: {random.uniform(40, 90):.1f}%
Active Data Processes: {random.randint(5, 20)}
Ongoing Analytics Jobs: {random.randint(1, 10)}
"""
            simulate_typing(summary)
        
        # Sleep for a random interval between 5 and 15 seconds
        time.sleep(random.uniform(5, 15))

if __name__ == "__main__":
    try:
        simulate_typing("Initializing lightweight data analysis environment simulation...")
        run_simulation()
    except KeyboardInterrupt:
        simulate_typing("\nShutting down simulation...")