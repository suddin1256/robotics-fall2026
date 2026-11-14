def decide(state, event):
    phase = state["phase"]
    kind = event["kind"]
    target = event["target"]

    active = phase in ("CLARIFY", "CONFIRM", "EXECUTING", "WAIT_READY")
    named_cup = target in ("red", "blue")

    if kind == "CANCEL" and active:
        return "cancel"

    if kind == "REQUEST" and phase in (
        "IDLE", "CLARIFY", "CONFIRM", "RECOVERY", "CANCELLED"
    ):
        return "select" if named_cup else "clarify"

    if kind == "CORRECT" and active and named_cup:
        return "select"

    if kind == "CONFIRM" and phase == "CONFIRM":
        return "begin"

    if kind == "TICK" and phase == "EXECUTING":
        return "advance"

    if kind == "READY" and phase == "WAIT_READY":
        return "release"

    if kind == "TIMEOUT" and phase == "WAIT_READY":
        return "timeout"

    return "hold"