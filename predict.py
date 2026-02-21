from pathlib import Path

def predict_structure(sequence, jobname="protein"):
    """
    Dummy prediction function for now.
    Later we will replace this with real ColabFold prediction.
    """

    # create results folder
    Path("results").mkdir(exist_ok=True)

    # fake PDB structure (simple helix example)
    pdb_content = f"""
ATOM      1  N   ALA A   1      11.104  13.207   9.300  1.00 20.00           N
ATOM      2  CA  ALA A   1      12.560  13.407   9.300  1.00 20.00           C
ATOM      3  C   ALA A   1      13.060  14.800   9.300  1.00 20.00           C
ATOM      4  O   ALA A   1      12.300  15.700   9.300  1.00 20.00           O
END
"""

    pdb_file = f"results/{jobname}.pdb"

    with open(pdb_file, "w") as f:
        f.write(pdb_content)

    return pdb_file
