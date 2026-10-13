# Parallel and Distributed Computing

A curated collection of parallel and distributed implementations using OpenMP, MPI, hybrid parallelism, and Hadoop MapReduce.

The implementations remain close to their original form. This repository brings them into one structure, preserves their histories, and documents the progression from shared-memory concurrency to distributed data processing.

## Contents

| Area | Implementations |
|---|---|
| OpenMP | [Thread discovery](openmp/thread-count) and a [shared-memory consensus](openmp/consensus) implementation |
| MPI | [Distributed consensus](mpi/consensus) across processes |
| Hybrid MPI + OpenMP | [Parallel search](hybrid/parallel-search) across worker processes and threads |
| Hadoop MapReduce | [Word count](mapreduce/word-count), [maximum temperature](mapreduce/max-temperature), [keyword analysis](mapreduce/keyword-analysis), and [average comment length](mapreduce/comment-length) |

## Toolchains

- C++17 compiler with OpenMP support
- Open MPI for MPI and hybrid programs
- Java and Hadoop MapReduce libraries for the MapReduce programs

Each component retains its original README and source layout. The repository CI validates the structure and compiles the native programs on Linux.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md). The original repositories did not declare licenses, so no blanket open-source license is introduced here.
