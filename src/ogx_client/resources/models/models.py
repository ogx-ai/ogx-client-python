# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from .openai import (
    OpenAIResource,
    AsyncOpenAIResource,
    OpenAIResourceWithRawResponse,
    AsyncOpenAIResourceWithRawResponse,
    OpenAIResourceWithStreamingResponse,
    AsyncOpenAIResourceWithStreamingResponse,
)
from ...types import model_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.model_list_response import ModelListResponse
from ...types.model_retrieve_response import ModelRetrieveResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def openai(self) -> OpenAIResource:
        return OpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        model_id: str,
        *,
        anthropic_version: str | Omit = omit,
        x_goog_api_client: str | Omit = omit,
        x_goog_api_key: str | Omit = omit,
        x_goog_user_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelRetrieveResponse:
        """Get a model by its identifier.

        Returns OpenAI, Anthropic, or Google response
        format based on SDK detection headers.

        Args:
          model_id: The ID of the model to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not model_id:
            raise ValueError(f"Expected a non-empty value for `model_id` but received {model_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-version": anthropic_version,
                    "x-goog-api-client": x_goog_api_client,
                    "x-goog-api-key": x_goog_api_key,
                    "x-goog-user-project": x_goog_user_project,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ModelRetrieveResponse,
            self._get(
                path_template("/v1/models/{model_id}", model_id=model_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        anthropic_version: str | Omit = omit,
        x_goog_api_client: str | Omit = omit,
        x_goog_api_key: str | Omit = omit,
        x_goog_user_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelListResponse:
        """List models.

        Returns OpenAI, Anthropic, or Google response format based on SDK
        detection headers.

        Args:
          after_id: Return models after this model ID (Anthropic SDK format only).

          before_id: Return models before this model ID (Anthropic SDK format only).

          limit: Maximum number of models to return (Anthropic SDK format only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-version": anthropic_version,
                    "x-goog-api-client": x_goog_api_client,
                    "x-goog-api-key": x_goog_api_key,
                    "x-goog-user-project": x_goog_user_project,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ModelListResponse,
            self._get(
                "/v1/models",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "after_id": after_id,
                            "before_id": before_id,
                            "limit": limit,
                        },
                        model_list_params.ModelListParams,
                    ),
                ),
                cast_to=cast(Any, ModelListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def openai(self) -> AsyncOpenAIResource:
        return AsyncOpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        model_id: str,
        *,
        anthropic_version: str | Omit = omit,
        x_goog_api_client: str | Omit = omit,
        x_goog_api_key: str | Omit = omit,
        x_goog_user_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelRetrieveResponse:
        """Get a model by its identifier.

        Returns OpenAI, Anthropic, or Google response
        format based on SDK detection headers.

        Args:
          model_id: The ID of the model to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not model_id:
            raise ValueError(f"Expected a non-empty value for `model_id` but received {model_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-version": anthropic_version,
                    "x-goog-api-client": x_goog_api_client,
                    "x-goog-api-key": x_goog_api_key,
                    "x-goog-user-project": x_goog_user_project,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ModelRetrieveResponse,
            await self._get(
                path_template("/v1/models/{model_id}", model_id=model_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        anthropic_version: str | Omit = omit,
        x_goog_api_client: str | Omit = omit,
        x_goog_api_key: str | Omit = omit,
        x_goog_user_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelListResponse:
        """List models.

        Returns OpenAI, Anthropic, or Google response format based on SDK
        detection headers.

        Args:
          after_id: Return models after this model ID (Anthropic SDK format only).

          before_id: Return models before this model ID (Anthropic SDK format only).

          limit: Maximum number of models to return (Anthropic SDK format only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-version": anthropic_version,
                    "x-goog-api-client": x_goog_api_client,
                    "x-goog-api-key": x_goog_api_key,
                    "x-goog-user-project": x_goog_user_project,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ModelListResponse,
            await self._get(
                "/v1/models",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "after_id": after_id,
                            "before_id": before_id,
                            "limit": limit,
                        },
                        model_list_params.ModelListParams,
                    ),
                ),
                cast_to=cast(Any, ModelListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.retrieve = to_raw_response_wrapper(
            models.retrieve,
        )
        self.list = to_raw_response_wrapper(
            models.list,
        )

    @cached_property
    def openai(self) -> OpenAIResourceWithRawResponse:
        return OpenAIResourceWithRawResponse(self._models.openai)


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.retrieve = async_to_raw_response_wrapper(
            models.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            models.list,
        )

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithRawResponse:
        return AsyncOpenAIResourceWithRawResponse(self._models.openai)


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.retrieve = to_streamed_response_wrapper(
            models.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            models.list,
        )

    @cached_property
    def openai(self) -> OpenAIResourceWithStreamingResponse:
        return OpenAIResourceWithStreamingResponse(self._models.openai)


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.retrieve = async_to_streamed_response_wrapper(
            models.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            models.list,
        )

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithStreamingResponse:
        return AsyncOpenAIResourceWithStreamingResponse(self._models.openai)
