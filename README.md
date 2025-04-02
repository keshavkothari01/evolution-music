# Evolution Music - Generating Music with Genetic Algorithms

## Introduction
Evolution Music is a project that uses genetic algorithms to evolve MIDI-based music compositions. By treating musical notes as a population, the algorithm applies selection, mutation, and crossover operations to gradually improve the generated music. The goal is to produce musically pleasing compositions through evolutionary processes.

## Features
- Genetic Algorithm-Based Music Generation: Uses selection, mutation, and crossover to evolve MIDI sequences.
- MIDI Note Encoding: Stores and manipulates MIDI notes using a compact integer representation.
- Automated Fitness Evaluation: Determines the quality of music based on predefined rules.
- MIDI Output Generation: Converts evolved sequences into MIDI files for playback.

## Project structure
evolution-music
├── PythonScripts
│   ├── evolveSong.py        # Main script for evolving music
│   ├── initPop.py           # Initializes the population
│   ├── fitnessFunc.py       # Evaluates the quality of generated music
│   ├── mutations.py         # Applies mutations to the population
│   ├── midiNote.py          # Handles MIDI note encoding and decoding
│   ├── writeNote.py         # Writes MIDI notes into a usable format
│   ├── bits2asc.py          # Converts binary data to ASCII for processing
│   ├── makeBestSong.sh      # Shell script to automate the pipeline
├── Output                   # Directory where final MIDI files are stored
└── README.md                # Project documentation

## Installation
Ensure you have the following installed: - Python 3 - Required Python libraries (mido, numpy, etc.) - GitHub CLI (for repository management)

## License
This project is licensed under the MIT License. See LICENSE for details.
