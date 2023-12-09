import subprocess
import os
import time

def run_game(exe_path):
    try:
        subprocess.Popen([exe_path], shell=True)
    except Exception as e:
        print(f"Error running {exe_path}: {e}")

if __name__ == "__main__":
    game1_name = "CALL OF RACE.exe"
    game2_name = "SPEEDY_MAQING_by_thug_hunter.exe"

    # Set the working directory to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Get the absolute paths for the games
    game1_path = os.path.abspath(game1_name)
    game2_path = os.path.abspath(game2_name)

    # Run CALL OF RACE.exe only once
    print(f"Running {game1_path}...")
    run_game(game1_path)

    while True:
        # Run SPEEDY_MAQING_by_thug_hunter.exe every ten seconds
        print(f"Running {game2_path}...")
        run_game(game2_path)

        print("Waiting for 20 seconds before running SPEEDY_MAQING_by_thug_hunter.exe again...")
        time.sleep(20)
