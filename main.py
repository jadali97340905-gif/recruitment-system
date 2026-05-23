import os

print("=== RECRUITMENT SYSTEM CONTROLLER ===")

print("\n1. Generating leads...")
os.system('python scripts\\generate_leads(1).py')

print("\n2. Processing leads...")
os.system('python scripts\\messenger(1).py')

print("\nSYSTEM COMPLETE")
