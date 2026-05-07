# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConversationDeleteResponse"]


class ConversationDeleteResponse(BaseModel):
    """Response for deleted conversation."""

    id: str
    """The deleted conversation identifier"""

    deleted: Optional[bool] = None
    """Whether the object was deleted"""

    object: Optional[Literal["conversation.deleted"]] = None
    """Object type"""
