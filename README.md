# Page Replacement Algorithms

This repository contains simulation programs for page replacement algorithms, specifically:

- **First-In, First-Out (FIFO)**
- **Least Recently Used (LRU)**

## Description

Page replacement algorithms are used in operating systems to manage memory pages in a virtual memory system. This repository provides Python implementations for FIFO and LRU page replacement strategies.

The programs simulate page replacement using randomly generated page reference strings and calculate average page faults.

## How to Use

1. Clone or download this repository to your local machine.
2. Each algorithm is implemented in a separate Python file:
   - `fifo.py`: Simulates the First-In, First-Out page replacement algorithm.
   - `lru.py`: Simulates the Least Recently Used page replacement algorithm.

3. Simply run the Python script of your choice to see the results. Example:

   To run FIFO:
   ```bash
   python fifo.py
   ```
   To run LRU:
   ```bash
   python lru.py
   ```

## Output

The programs will generate example data and print the results, including:
- **Average page faults**

The data used in these simulations is randomly generated, and the results will vary each time you run the program.
