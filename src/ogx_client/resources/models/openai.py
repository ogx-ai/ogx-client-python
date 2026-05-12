# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.models import openai_list_params
from ...types.models.openai_list_response import OpenAIListResponse

__all__ = ["OpenAIResource", "AsyncOpenAIResource"]


class OpenAIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#accessing-raw-response-data-eg-headers
        """
        return OpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#with_streaming_response
        """
        return OpenAIResourceWithStreamingResponse(self)

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
    ) -> OpenAIListResponse:
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
            OpenAIListResponse,
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
                        openai_list_params.OpenAIListParams,
                    ),
                ),
                cast_to=cast(
                    Any, OpenAIListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncOpenAIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ogx-ai/ogx-client-python#with_streaming_response
        """
        return AsyncOpenAIResourceWithStreamingResponse(self)

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
    ) -> OpenAIListResponse:
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
            OpenAIListResponse,
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
                        openai_list_params.OpenAIListParams,
                    ),
                ),
                cast_to=cast(
                    Any, OpenAIListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class OpenAIResourceWithRawResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

        self.list = to_raw_response_wrapper(
            openai.list,
        )


class AsyncOpenAIResourceWithRawResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

        self.list = async_to_raw_response_wrapper(
            openai.list,
        )


class OpenAIResourceWithStreamingResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

        self.list = to_streamed_response_wrapper(
            openai.list,
        )


class AsyncOpenAIResourceWithStreamingResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

        self.list = async_to_streamed_response_wrapper(
            openai.list,
        )
