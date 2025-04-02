import subprocess

# Step 1: Initialize Population
print("Initializing Population...")
subprocess.run(["python3", "initPop.py"])

# Step 2: Evolve the Population
print("Evolving Songs...")
subprocess.run(["python3", "evolveSong.py"])

# Step 3: Evaluate Fitness
print("Evaluating Fitness...")
subprocess.run(["python3", "fitnessFunc.py"])

# Step 4: Generate MIDI from Best Song
print("Generating Best Song MIDI...")
subprocess.run(["python3", "writeNote.py"])

print("Pipeline Completed! Check the output folder for the generated MIDI file.")
