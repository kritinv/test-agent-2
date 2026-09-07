from importlib import util
from pathlib import Path

# Keep this file at the repo root, keep the function named run(input), and
# return the app output as a string so Confident scores the real answer.
_AGENT_PATH = Path(__file__).parent / "agents" / "02-code-review-agent" / "agent.py"
_SPEC = util.spec_from_file_location("code_review_agent", _AGENT_PATH)
assert _SPEC and _SPEC.loader
_AGENT = util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_AGENT)


def run(input):
    return str(_AGENT.review_code(str(input)))
