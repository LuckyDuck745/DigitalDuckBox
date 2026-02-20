import time
import random

def run_diagnostic():
    print("🚀 --- INITIALIZING DUCK-SCAN v1.0 ---")
    time.sleep(1)
    
    # List of "systems" to check
    systems = [
        "Buoyancy Control", 
        "Feather Integrity", 
        "Quack Frequency", 
        "Breadcrumb Storage",
        "Navigation Compass"
    ]
    
    for system in systems:
        # Randomly pick a status
        status = random.choice(["OPTIMAL", "STABLE", "QUACKING", "NEEDS BREAD"])
        load = random.randint(10, 95)
        
        print(f"[#] Checking {system}...")
        time.sleep(0.6) # Makes it look like it's actually thinking
        print(f"    STATUS: {status} | SYSTEM LOAD: {load}%")
    
    print("\n✅ DIAGNOSTIC COMPLETE. ALL SYSTEMS ARE QUACKING.")

if __name__ == "__main__":
    run_diagnostic()
