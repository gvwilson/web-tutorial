"""Database migration."""

import argparse
from pathlib import Path
import re
import sqlite3
import sys


PATTERNS = {
    "bwd": re.compile(r"^(\d+)_bwd_(.+)"),
    "check": re.compile(r"^(\d+)_check_(.+)"),
    "fwd": re.compile(r"^(\d+)_fwd_(.+)"),
}


def main():
    """Main driver."""
    opt = parse_args()
    connection = sqlite3.connect(opt.db)
    if opt.forward:
        direction = "fwd"
    elif opt.backward:
        direction = "bwd"
    else:
        assert False, f"Unknown direction"
    migrations = get_migrations(opt.migrations, direction, opt.limit)
    if opt.forward:
        for filename in migrations:
            migrate(connection, filename, opt.verbose)
    elif opt.backward:
        for filename in reversed(migrations):
            migrate(connection, filename, opt.verbose)


def get_migrations(dirpath, direction, limit):
    """Find migration files."""
    pat = PATTERNS[direction]
    result = []
    for filepath in sorted(Path(dirpath).glob("*.sql")):
        m = pat.match(str(filepath.name))
        if not m:
            continue
        if limit and (m.group(1) > limit):
            continue
        result.append(filepath)
        check = Path(filepath.parent, f"{m.group(1)}_check_{m.group(2)}")
        result.append(check)
    return result


def migrate(connection, filename, verbose):
    """Apply migration."""
    if verbose:
        print(f"migrating {filename}")
    connection.executescript(filename.read_text())


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--backward", action="store_true", help="migrate backward")
    parser.add_argument("--db", required=True, help="database file")
    parser.add_argument("--forward", action="store_true", help="migrate forward")
    parser.add_argument("--migrations", type=str, required=True, help="migrations directory")
    parser.add_argument("--limit", type=str, help="how far to go or where to start regression")
    parser.add_argument("--verbose", action="store_true", help="report progress")
    opt = parser.parse_args()

    if (opt.backward + opt.forward) != 1:
        print("Must specify exactly one of --forward or --backward")
        sys.exit(1)

    return opt


if __name__ == "__main__":
    main()

