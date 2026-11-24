def handle_create(payload):
    return {"created": payload}


def handle_delete(payload):
    return {"deleted": payload}


def handle_legacy_export(payload):
    return {"exported": payload}


def _old_helper(value):
    return str(value).strip().lower()
