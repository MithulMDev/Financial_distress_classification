import random
import time
import threading
import multiprocessing
import pyautogui
import subprocess
from datetime import datetime
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pygetwindow as gw

# Websites for browsing simulation
websites = ["http://example1.com", "http://example2.com", "http://example3.com"]

# Application names for switching
applications = ["Docker", "SQL Server Management Studio", "PostgreSQL"]

# Setup browser driver
def setup_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Browser Simulation
def simulate_browsing():
    driver = setup_driver()
    try:
        while True:
            site = random.choice(websites)
            driver.get(site)
            time.sleep(random.randint(10, 60))  # Stay on the site for 10 to 60 seconds

            # Simulate light interaction
            if random.random() < 0.5:
                for _ in range(random.randint(1, 3)):
                    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(random.uniform(2, 5))
            
            driver.quit()
            time.sleep(random.randint(900, 1800))  # Wait between 15 to 30 minutes before reopening
            driver = setup_driver()
    except KeyboardInterrupt:
        driver.quit()

# Mouse Activity
screenWidth, screenHeight = pyautogui.size()

def move_mouse():
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.5))

def random_click():
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.5))
    pyautogui.click()

def simulate_mouse_activity():
    try:
        while True:
            move_mouse()
            time.sleep(random.randint(5, 15))  # Move cursor every 5 to 15 seconds
            if random.random() < 0.3:  # 30% chance to click
                random_click()
                time.sleep(random.uniform(2, 5))  # Small delay after clicking
    except KeyboardInterrupt:
        pass

# Keyboard Activity
def type_text():
    text = ["test", "dummy", "sample"]
    pyautogui.typewrite(random.choice(text), interval=random.uniform(0.05, 0.1))

def simulate_keyboard_activity():
    try:
        while True:
            type_text()
            time.sleep(random.randint(30, 120))  # Type text every 30 to 120 seconds
    except KeyboardInterrupt:
        pass

# Terminal Simulation
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

def simulate_typing(text, min_delay=0.50, max_delay=1.25):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
    print()

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

def run_terminal_simulation():
    start_time = datetime.now()
    try:
        simulate_typing("Initializing lightweight data analysis environment simulation...")
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
            
            # Sleep for a random interval between 5 and 10 seconds
            time.sleep(random.uniform(5, 10))
    except KeyboardInterrupt:
        simulate_typing("\nShutting down simulation...")

# Application Switching
def open_application(name):
    if name == "Docker":
        subprocess.Popen("docker", shell=True)
    elif name == "SQL Server Management Studio":
        subprocess.Popen("ssms", shell=True)
    elif name == "PostgreSQL":
        subprocess.Popen("pgadmin4", shell=True)

def close_application(name):
    if name == "Docker":
        subprocess.Popen("taskkill /F /IM docker.exe", shell=True)
    elif name == "SQL Server Management Studio":
        subprocess.Popen("taskkill /F /IM ssms.exe", shell=True)
    elif name == "PostgreSQL":
        subprocess.Popen("taskkill /F /IM pgAdmin4.exe", shell=True)

def switch_application():
    while True:
        app = random.choice(applications)
        windows = gw.getWindowsWithTitle(app)
        if windows:
            windows[0].activate()
            pyautogui.moveTo(random.randint(0, screenWidth), random.randint(0, screenHeight), duration=random.uniform(0.2, 0.5))
            time.sleep(random.uniform(0.5, 2.0))  # Pause before clicking
            pyautogui.click()
            time.sleep(random.randint(10, 30))  # Stay in the app for a random interval

        # Randomly open or close applications
        if random.random() < 0.5:
            open_application(app)
        else:
            close_application(app)
        time.sleep(random.randint(300, 600))  # Switch applications every 5 to 10 minutes

# Main
if __name__ == "__main__":
    # Create threads for browsing, mouse, keyboard, and application switching activities
    browsing_thread = threading.Thread(target=simulate_browsing)
    mouse_thread = threading.Thread(target=simulate_mouse_activity)
    keyboard_thread = threading.Thread(target=simulate_keyboard_activity)
    app_switch_thread = threading.Thread(target=switch_application)

    # Create a process for terminal simulation
    terminal_process = multiprocessing.Process(target=run_terminal_simulation)

    # Start the threads and process
    browsing_thread.start()
    mouse_thread.start()
    keyboard_thread.start()
    app_switch_thread.start()
    terminal_process.start()

    # Join the threads
    browsing_thread.join()
    mouse_thread.join()
    keyboard_thread.join()
    app_switch_thread.join()

    # Join the process
    terminal_process.join()
