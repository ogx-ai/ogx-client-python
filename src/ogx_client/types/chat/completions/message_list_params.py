# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: Optional[str]
    """Identifier for the last message from the previous pagination request."""

    limit: Optional[int]
    """Number of messages to retrieve."""

    order: Optional[Literal["asc", "desc"]]
    """Sort order for messages by timestamp. Use "asc" or "desc". Defaults to "asc"."""
