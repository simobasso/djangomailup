"""MailUp Utils."""


def response_parser(response):
    """
    Parse response from json to dict.

    If an error in the response data an exception is raised
    """
    try:
        data = response.json()
    except ValueError:
        raise Exception(
            "'response' is not JSON serializable: '{}'".format(response.text)
        )
    if "error" in data:
        raise Exception("{error}: {description}".format(
            error=data["error"],
            description=data["error_description"]
        ))
    return data
