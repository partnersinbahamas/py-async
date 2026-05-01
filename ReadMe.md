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


------


# Parallelism

Parallelism is a concept in programming where multiple tasks are executed truly at the same time, typically using multiple CPU cores or processors.

The main goal of parallelism is to increase performance by dividing work into smaller parts and processing them simultaneously.

### 📌 Important to understand

Parallelism is about actual simultaneous execution (multiple cores)
Concurrency is about structuring tasks (how they are interleaved)

### 🔹 Types of Parallelism (Execution Model)
- #### Thread-based Parallelism
  - Uses threads within a single process
  - Threads share the same memory space
  - Lightweight compared to processes
  - Multithreading in many applications

#### Process-based Parallelism
  - Uses separate processes
  - Each process has its own memory space