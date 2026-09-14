import time
import schedule
import subprocess

print("\n--- Testing Native Python Task Scheduler ---")

run_count = 0


def run_inventory_job():
    global run_count
    run_count += 1
    print(f"[{time.strftime('%H:%M:%S')}] Executing Scheduled Task #{run_count}...")

    # Run the SQLite inventory check script we created earlier
    cmd = [
        r"C:\Users\saifh\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe",
        r"C:\Users\saifh\agent_workspace\test_database.py"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("  -> Task completed: Database queried successfully.")
    else:
        print(f"  -> Task failed: {res.stderr}")


# Schedule the job to run every 3 seconds for testing
schedule.every(3).seconds.do(run_inventory_job)

print("Scheduler started. Running 2 automated cycles then stopping cleanly...\n")

# Run 2 iterations then exit safely
while run_count < 2:
    schedule.run_pending()
    time.sleep(1)

print("\n[SUCCESS] Scheduler verified: 2 cycles completed without OS freezing.")