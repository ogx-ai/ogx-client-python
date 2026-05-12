# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..list_models_response import ListModelsResponse

__all__ = [
    "OpenAIListResponse",
    "AnthropicListModelsResponse",
    "AnthropicListModelsResponseData",
    "GoogleListModelsResponse",
    "GoogleListModelsResponseModel",
]


class AnthropicListModelsResponseData(BaseModel):
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


class AnthropicListModelsResponse(BaseModel):
    """Response containing a list of Anthropic model objects."""

    data: List[AnthropicListModelsResponseData]
    """List of Anthropic model objects."""

    first_id: Optional[str] = None
    """First ID in the data list, usable as before_id for the previous page."""

    has_more: Optional[bool] = None
    """Whether there are more results in the requested page direction."""

    last_id: Optional[str] = None
    """Last ID in the data list, usable as after_id for the next page."""


class GoogleListModelsResponseModel(BaseModel):
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


class GoogleListModelsResponse(BaseModel):
    """Response containing a list of Google model objects."""

    models: List[GoogleListModelsResponseModel]
    """List of Google model objects."""


OpenAIListResponse: TypeAlias = Union[ListModelsResponse, AnthropicListModelsResponse, GoogleListModelsResponse]
