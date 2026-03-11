from pathlib import Path
import subprocess
import sys  # Add this

# repo root
repo_root = Path(__file__).parent.parent.parent.resolve()  # .github/scripts -> repo root

def main():
    python_exe = sys.executable  # ensures the same Python as workflow

    print("Decrypting submission...")
    subprocess.run([python_exe, str(repo_root / "encryption" / "decrypt.py")], check=True)

    print("Scoring submission...")
    subprocess.run([python_exe, str(repo_root / "leaderboard" / "score_submission.py")], check=True)

    print("Updating leaderboard...")
    subprocess.run([python_exe, str(repo_root / "leaderboard" / "update_leaderboard.py")], check=True)

if __name__ == "__main__":
    main()
