import random
import csv
import os

NUM_LEADS = 100  # start SMALL for testing

AREA_CODES = ["514", "438", "450", "418", "819"]

def make_number():
    return f"+1-{random.choice(AREA_CODES)}-{random.randint(200,999)}-{random.randint(1000,9999)}"

def generate():
    leads = []
    for i in range(NUM_LEADS):
        leads.append([i+1, make_number(), "NEW"])
    return leads

def save(leads):
    os.makedirs("data", exist_ok=True)
    with open("data/leads.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Phone", "Status"])
        writer.writerows(leads)

if __name__ == "__main__":
    data = generate()
    save(data)
    print("DONE: leads generated")
