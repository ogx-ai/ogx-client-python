# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ogx_client import OgxClient, AsyncOgxClient
from tests.utils import assert_matches_type
from ogx_client.pagination import SyncOpenAICursorPage, AsyncOpenAICursorPage
from ogx_client.types.chat.completions import MessageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OgxClient) -> None:
        message = client.chat.completions.messages.list(
            completion_id="completion_id",
        )
        assert_matches_type(SyncOpenAICursorPage[MessageListResponse], message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OgxClient) -> None:
        message = client.chat.completions.messages.list(
            completion_id="completion_id",
            after="after",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncOpenAICursorPage[MessageListResponse], message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OgxClient) -> None:
        response = client.chat.completions.messages.with_raw_response.list(
            completion_id="completion_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncOpenAICursorPage[MessageListResponse], message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OgxClient) -> None:
        with client.chat.completions.messages.with_streaming_response.list(
            completion_id="completion_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncOpenAICursorPage[MessageListResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `completion_id` but received ''"):
            client.chat.completions.messages.with_raw_response.list(
                completion_id="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOgxClient) -> None:
        message = await async_client.chat.completions.messages.list(
            completion_id="completion_id",
        )
        assert_matches_type(AsyncOpenAICursorPage[MessageListResponse], message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOgxClient) -> None:
        message = await async_client.chat.completions.messages.list(
            completion_id="completion_id",
            after="after",
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncOpenAICursorPage[MessageListResponse], message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOgxClient) -> None:
        response = await async_client.chat.completions.messages.with_raw_response.list(
            completion_id="completion_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncOpenAICursorPage[MessageListResponse], message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOgxClient) -> None:
        async with async_client.chat.completions.messages.with_streaming_response.list(
            completion_id="completion_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncOpenAICursorPage[MessageListResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOgxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `completion_id` but received ''"):
            await async_client.chat.completions.messages.with_raw_response.list(
                completion_id="",
            )
