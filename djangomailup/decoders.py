"""MailUp Decoder."""


def mailup_token_request(r, key):
    """Procecess Token and error."""
    data = r.json()
    if "error" in data:
        raise Exception("{error}: {description}".format(
            error=data["error"],
            description=data["error_description"]
        ))
    if key not in data:
        raise KeyError("Key {key} not in: {raw}".format(
            key=key,
            raw=r.content
        ))

    return data[key]
