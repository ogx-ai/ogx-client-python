# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ogx_client import OgxClient, AsyncOgxClient
from tests.utils import assert_matches_type
from ogx_client.types.models import OpenAIListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpenAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OgxClient) -> None:
        openai = client.models.openai.list()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OgxClient) -> None:
        openai = client.models.openai.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_version="anthropic-version",
            x_goog_api_client="x-goog-api-client",
            x_goog_api_key="x-goog-api-key",
            x_goog_user_project="x-goog-user-project",
        )
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OgxClient) -> None:
        response = client.models.openai.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OgxClient) -> None:
        with client.models.openai.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAIListResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpenAI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOgxClient) -> None:
        openai = await async_client.models.openai.list()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOgxClient) -> None:
        openai = await async_client.models.openai.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_version="anthropic-version",
            x_goog_api_client="x-goog-api-client",
            x_goog_api_key="x-goog-api-key",
            x_goog_user_project="x-goog-user-project",
        )
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.models.openai.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOgxClient) -> None:
        async with async_client.models.openai.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAIListResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True
