from colabfold.batch import run
from pathlib import Path

def predict_structure(sequence, jobname="protein"):

    # --- Save sequence to FASTA ---
    Path("results").mkdir(exist_ok=True)
    fasta_file = f"results/{jobname}.fasta"
    with open(fasta_file, "w") as f:
        f.write(f">{jobname}\n{sequence}")

    # --- Run ColabFold ---
    run(
        input_fasta_path=fasta_file,
        result_dir="results",
        model_type="alphafold2_ptm",
        num_models=1,
        num_recycles=3,
        use_gpu=True,   # if GPU available
        verbose=True
    )

    # ColabFold outputs unrelaxed PDBs
    pdb_file = f"results/{jobname}/{jobname}_unrelaxed_rank_001.pdb"
    return pdb_file
