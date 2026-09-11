import json
from pathlib import Path


def main() -> None:
    lines = Path("eval/dataset.jsonl").read_text(encoding="utf-8").splitlines()
    rows = [json.loads(line) for line in lines]
    print(f"Loaded {len(rows)} evaluation case(s). Add provider calls and scoring here.")


if __name__ == "__main__":
    main()
