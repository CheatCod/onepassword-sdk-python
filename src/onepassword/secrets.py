from .core import _invoke
from json import loads

"""Secrets represents all operations the SDK client can perform on 1Password secrets."""


class Secrets:
    def __init__(self, client_id):
        self.client_id = client_id

    """resolve returns the secret the provided reference points to."""

    async def resolve(self, secret_reference):
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "Resolve",
                    "parameters": {
                        "secret_reference": secret_reference,
                    },
                },
            }
        )
        return loads(response)
