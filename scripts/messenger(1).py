import csv
import os

INPUT_FILE = "data/leads.csv"
OUTPUT_FILE = "data/leads_updated.csv"

def load_leads():
    leads = []

    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)

    return leads

def process_leads(leads):
    updated = []

    for lead in leads:
        # SIMULATED LOGIC
        if lead["Status"] == "NEW":
            lead["Status"] = "CONTACTED"
            lead["Messages_Sent"] = "1"
            lead["Last_Action"] = "Initial outreach sent"

        updated.append(lead)

    return updated

def save_leads(leads):
    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=leads[0].keys())
        writer.writeheader()
        writer.writerows(leads)

if __name__ == "__main__":
    leads = load_leads()
    updated = process_leads(leads)
    save_leads(updated)

    print("DONE: leads processed and updated")
