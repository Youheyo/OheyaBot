clear

$SCRIPT_DIR = $PSScriptRoot

Write-Host "Starting OheyaBot"

cd $SCRIPT_DIR

./.venv/Scripts/activate

./.venv/Scripts/python main.py
