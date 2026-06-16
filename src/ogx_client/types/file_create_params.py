# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to upload."""

    purpose: Required[Literal["assistants", "batch", "fine-tune", "vision", "user_data", "evals"]]
    """The intended purpose of the uploaded file."""

    expires_after: Optional[str]
    """Optional expiration settings for the file."""
