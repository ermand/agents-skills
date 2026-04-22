#!/usr/bin/env python3

import json
import subprocess
import sys
from pathlib import Path


def main():
    try:
        # Read input data from stdin
        input_data = json.load(sys.stdin)

        tool_input = input_data.get("tool_input", {})

        # Get file path from tool input
        file_path = tool_input.get("file_path")
        if not file_path:
            sys.exit(0)

        # Only check TypeScript/JavaScript files
        if not file_path.endswith((".ts", ".tsx", ".js", ".jsx")):
            sys.exit(0)

        # Check if file exists
        if not Path(file_path).exists():
            sys.exit(0)

        # Run oxlint to check for errors
        try:
            result = subprocess.run(
                ["bunx", "oxlint", file_path],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0 and (result.stdout or result.stderr):
                error_output = result.stdout or result.stderr

                # Only fail if actual errors found (not just warnings)
                if "Found 0 warnings and 0 errors" not in error_output:
                    print(f"oxlint errors found in {file_path}:", file=sys.stderr)
                    print(error_output, file=sys.stderr)
                    sys.exit(2)

        except subprocess.TimeoutExpired:
            print("oxlint check timed out", file=sys.stderr)
            sys.exit(0)
        except FileNotFoundError:
            # oxlint not available, skip check
            sys.exit(0)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error in oxlint hook: {e}", file=sys.stderr)
        sys.exit(1)


main()
