# Concurrency
Concurrency is a concept in programming where multiple tasks are executed “at the same time”, meaning their execution overlaps in time. However, tasks do not necessarily run in parallel — they may simply switch rapidly between each other.

The main goal of concurrency is to efficiently utilize resources (CPU, waiting time, input/output) and make programs more responsive.

### 📌 Important to understand
Concurrency is about structuring tasks (how they are interleaved)
Parallelism is about actual simultaneous execution (on multiple cores)

### 🔹 Types of Concurrency
- #### Cooperative Concurrency
    - Tasks voluntarily yield control
    - Context switching happens explicitly (e.g., using await)

- #### Preemptive Concurrency
  - The operating system controls task switching
  - Threads can be interrupted at any moment

-------

## CPU-bound tasks
- Limited by the CPU’s processing power
- Benefit more from parallelism (multiple cores)
- Examples: heavy computations, data processing, rendering

## I/O-bound tasks
- Limited by waiting time (network, disk, database)
- Benefit from concurrency (e.g., async/await)
- Examples: API calls, file reading, database queries