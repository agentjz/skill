from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "downloads"
OUTPUT_FILE = OUTPUT_DIR / "skill.zip"

INCLUDED_FILES = [
    "skill.md",
    "README.md",
    "AGENTS.md",
    "spec.md",
    "plan.example.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "LICENSE",
    ".gitignore",
    ".codex/skills/project-development/SKILL.md",
    ".codex/skills/plan/SKILL.md",
]


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    with ZipFile(OUTPUT_FILE, "w", ZIP_DEFLATED) as archive:
        for relative_name in INCLUDED_FILES:
            path = ROOT / relative_name
            if not path.exists():
                raise FileNotFoundError(path)
            archive.write(path, relative_name)
    print(f"created {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
