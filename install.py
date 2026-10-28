#!/usr/bin/env python3
"""Install the bundled cianppt skill locally without network or extra packages."""

import argparse
from pathlib import Path
import shutil
import sys


SKILL_NAME = "cianppt"
SKILL_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/layout-recipes.md",
    "references/figures-and-literature.md",
    "references/research-storyline.md",
    "references/figurecode-workflow.md",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.home() / ".agents" / "skills",
        help="Parent skill directory (default: ~/.agents/skills)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Check without writing")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    target = args.dest.expanduser().resolve() / SKILL_NAME

    # Check the complete package before creating anything at the destination.
    for relative in SKILL_FILES:
        path = source / relative
        if not path.is_file() or path.is_symlink():
            parser.exit(1, f"Missing or unsupported package file: {relative}\n")
    entrypoint = (source / "SKILL.md").read_text(encoding="utf-8-sig")
    frontmatter = entrypoint.split("---", 2)
    if len(frontmatter) != 3 or "name: cianppt" not in frontmatter[1].splitlines():
        parser.exit(1, "SKILL.md does not identify the cianppt skill.\n")
    if target.exists() or target.is_symlink():
        parser.exit(1, f"Destination already exists; no files changed: {target}\n")
    if args.dry_run:
        print(f"Ready to install {len(SKILL_FILES)} files to: {target}")
        return 0

    target.mkdir(parents=True, exist_ok=False)
    for relative in SKILL_FILES:
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, destination)
    print(f"Installed cianppt to: {target}")
    print("Invoke $cianppt in your next Codex turn; restart if it is not discovered.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except OSError as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        sys.exit(1)
