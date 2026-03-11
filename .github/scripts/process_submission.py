# .github/scripts/process_submission.py
from pathlib import Path
import subprocess
import sys

repo_root = Path(__file__).parent.parent.parent.resolve()  # .github/scripts -> repo root

def main():
    python_exe = sys.executable

    submissions_dir = repo_root / "submissions"
    if not submissions_dir.exists():
        print("No submissions directory found")
        return

    print("Decrypting and scoring submissions...")

    # Run update_leaderboard.py which handles decryption and scoring
    subprocess.run(
        [python_exe, str(repo_root / "leaderboard/update_leaderboard.py")],
        check=True
    )

    print("Processing complete!")

if __name__ == "__main__":
    main()
