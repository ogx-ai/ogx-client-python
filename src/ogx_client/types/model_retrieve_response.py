# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelRetrieveResponse", "Model", "AnthropicModelInfo", "GoogleModelInfo"]


class Model(BaseModel):
    """A model resource representing an AI model registered in OGX."""

    id: str
    """The model identifier (OpenAI-compatible alias for identifier)."""

    identifier: str
    """Unique identifier for this resource in ogx"""

    object: Literal["model"]
    """The object type, always 'model'."""

    provider_id: str
    """ID of the provider that owns this resource"""

    created: Optional[int] = None
    """The Unix timestamp in seconds when the model was created."""

    metadata: Optional[Dict[str, builtins.object]] = None
    """Any additional metadata for this model"""

    api_model_type: Optional[Literal["llm", "embedding", "rerank"]] = FieldInfo(alias="model_type", default=None)
    """Enumeration of supported model types in OGX."""

    api_model_validation: Optional[bool] = FieldInfo(alias="model_validation", default=None)
    """Enable model availability check during registration.

    When false (default), validation is deferred to runtime and model is preserved
    during provider refresh.
    """

    owned_by: Optional[str] = None
    """The owner of the model."""

    provider_resource_id: Optional[str] = None
    """Unique identifier for this resource in the provider"""

    type: Optional[Literal["model"]] = None


class AnthropicModelInfo(BaseModel):
    """Anthropic model info response object.

    :id: Unique model identifier
    """

    id: str
    """Unique model identifier."""

    created_at: str
    """RFC 3339 datetime string representing when the model was released."""

    display_name: str
    """A human-readable name for the model."""

    max_input_tokens: Optional[int] = None
    """Maximum input context window size in tokens."""

    max_tokens: Optional[int] = None
    """Maximum value for the max_tokens parameter when using this model."""

    type: Optional[Literal["model"]] = None
    """Object type, always 'model'."""


class GoogleModelInfo(BaseModel):
    """Google model info response object.

    :name: Model resource name, e.g. 'models/gemini-pro'
    :display_name: A human-readable name for the model
    :description: A description of the model
    """

    display_name: str
    """A human-readable name for the model."""

    name: str
    """Model resource name, e.g. 'models/gemini-pro'."""

    description: Optional[str] = None
    """A description of the model."""


ModelRetrieveResponse: TypeAlias = Union[Model, AnthropicModelInfo, GoogleModelInfo]
