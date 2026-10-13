<h1 align="center">Searching a Number Among Slave Processes Using OpenMP and MPI</h1>

### Description
Program written in `C++ language` to search a number from an array after distributing it equally to all `Slave Processes` and using `OpenMP` and `MPI` for `Parallel Searching`. The detailed [project statement](Project%20Statement.pdf) is retained with the implementation.

### Manual
1) Use following command to `Compile the Code`:
    ```
    mpic++ -fopenmp Source.cpp -o Source
    ```

2) Use following command to `Execute the Code`. 3 indicates total number of processes to create:
    ```
    mpiexec -n 3 -f machinefile ./Source
    ```
    
### Working Screenshots
<div align="center">
  <img src="extras/working-ss-1.png" alt="Parallel search setup" width="700px"/>
</div>
<br/>
<div align="center">
  <img src="extras/working-ss-2.png" alt="Parallel search result" width="700px"/>
</div>
