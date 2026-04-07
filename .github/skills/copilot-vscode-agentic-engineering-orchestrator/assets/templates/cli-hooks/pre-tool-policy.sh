#!/usr/bin/env bash
set -euo pipefail
payload=$(cat)
command=$(printf '%s' "$payload" | sed -n 's/.*"command":"\([^"]*\)".*/\1/p')
case "$command" in
  *"rm -rf /"*|*"curl "*"| bash"*|*"sudo "*)
    echo "Blocked by repository policy: high-risk command pattern detected." >&2
    exit 2
    ;;
  *)
    exit 0
    ;;
esac
