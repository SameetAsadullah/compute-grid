<h1 align="center">Searching a Number Among Slave Processes Using OpenMP and MPI</h1>

### Description
A hybrid C++ search that partitions an array across MPI workers and uses OpenMP within each process. The supporting [system specification](docs/system-specification.pdf) is retained with the implementation.

### Manual
1) Use following command to `Compile the Code`:
    ```
    mpic++ -fopenmp main.cpp -o parallel-search
    ```

2) Use following command to `Execute the Code`. 3 indicates total number of processes to create:
    ```
    mpiexec -n 3 -f machinefile ./parallel-search
    ```
    
### Working Screenshots
<div align="center">
  <img src="extras/working-ss-1.png" alt="Parallel search setup" width="700px"/>
</div>
<br/>
<div align="center">
  <img src="extras/working-ss-2.png" alt="Parallel search result" width="700px"/>
</div>
