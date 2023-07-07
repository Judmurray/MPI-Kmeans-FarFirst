#!/bin/bash
#SBATCH -A cmda3634_rjh
#SBATCH -p normal_q
#SBATCH -t 00:10:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4
#SBATCH -o mpi_farfirst_debug.out

# Go to the directory where the job was submitted
cd $SLURM_SUBMIT_DIR

# Load the modules
module load matplotlib

# Build the executable
mpicc -D DEBUG -o mpi_kmeans mpi_kmeans.c mat.c vec.c

# run mpi_kmeans
mpiexec -np $SLURM_NTASKS --map-by ppr:$SLURM_NTASKS_PER_NODE:node ./mpi_kmeans 25 0

# The script will exit whether we give the "exit" command or not.
exit
