# Compute Grid

Parallel and distributed programs built with OpenMP, MPI, hybrid execution, and Hadoop MapReduce.

The workloads span shared-memory coordination, distributed processes, and data-parallel processing. Native components are validated on Linux.

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

Each component has its own README and source layout. Repository CI checks the structure and compiles the native programs on Linux.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for source history and licensing. No repository-wide open-source license is declared.
