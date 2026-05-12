# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OpenAIListParams"]


class OpenAIListParams(TypedDict, total=False):
    after_id: Optional[str]
    """Return models after this model ID (Anthropic SDK format only)."""

    before_id: Optional[str]
    """Return models before this model ID (Anthropic SDK format only)."""

    limit: Optional[int]
    """Maximum number of models to return (Anthropic SDK format only)."""

    anthropic_version: Annotated[str, PropertyInfo(alias="anthropic-version")]

    x_goog_api_client: Annotated[str, PropertyInfo(alias="x-goog-api-client")]

    x_goog_api_key: Annotated[str, PropertyInfo(alias="x-goog-api-key")]

    x_goog_user_project: Annotated[str, PropertyInfo(alias="x-goog-user-project")]
