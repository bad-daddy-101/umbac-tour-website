import json
from pathlib import Path

BASE_DIR = Path(r"D:\UMBAC Tour Website\assets\season-1")
OUTPUT_FILE = Path(r"D:\UMBAC Tour Website\data\season-1-rosters.json")

def slugify(name):
    return (
        name.lower()
        .replace("&", "and")
        .replace(" ", "-")
    )

teams = []

for team_dir in sorted(BASE_DIR.iterdir()):
    if not team_dir.is_dir():
        continue

    team_name = team_dir.name

    logo_exists = (team_dir / "logo.png").exists()

    players_dir = team_dir / "players"

    players = []

    if players_dir.exists():
        for player_file in sorted(players_dir.glob("*.png")):
            players.append({
                "name": player_file.stem,
                "file": player_file.name
            })

    teams.append({
        "name": team_name,
        "slug": slugify(team_name),
        "logo": "logo.png" if logo_exists else None,
        "playerCount": len(players),
        "players": players
    })

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE.write_text(
    json.dumps(
        {
            "season": 1,
            "year": 2024,
            "teams": teams
        },
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)

print()
print("Season 1 roster manifest generated:")
print(OUTPUT_FILE)
print()
print(f"Teams found: {len(teams)}")
print(f"Total player photos: {sum(len(t['players']) for t in teams)}")