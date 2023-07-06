# Copyright (c) 2021, VRAI Labs and/or its affiliates. All rights reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License") as published by the Apache Software Foundation.
#
# You may not use this file except in compliance with the License. You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from re import sub
from typing import Any, Dict, Optional
from jwt import encode  # type: ignore
from time import time
<<<<<<< HEAD

from ..provider import (
    Provider,
    ProviderConfigForClientType,
    ProviderInput,
||||||| 37d58eb3
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Union

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from httpx import AsyncClient
from jwt import decode, encode
from jwt.algorithms import RSAAlgorithm
from supertokens_python.recipe.thirdparty.api.implementation import (
    get_actual_client_id_from_development_client_id,
=======
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Union
from httpx import AsyncClient
from jwt import decode, encode

# You must have cryptography library installed for these imports to work:
from jwt.algorithms import RSAAlgorithm
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

from supertokens_python.recipe.thirdparty.api.implementation import (
    get_actual_client_id_from_development_client_id,
>>>>>>> 0.14
)
from .custom import GenericProvider, NewProvider
from .utils import get_actual_client_id_from_development_client_id


class AppleImpl(GenericProvider):
    async def get_config_for_client_type(
        self, client_type: Optional[str], user_context: Dict[str, Any]
    ) -> ProviderConfigForClientType:
        config = await super().get_config_for_client_type(client_type, user_context)

        if config.scope is None:
            config.scope = ["openid", "email"]

        if config.client_secret is None:
            config.client_secret = await self._get_client_secret(config)

        return config

    async def _get_client_secret(self, config: ProviderConfigForClientType) -> str:
        if (
            config.additional_config is None
            or config.additional_config.get("keyId") is None
            or config.additional_config.get("teamId") is None
            or config.additional_config.get("privateKey") is None
        ):
            raise Exception(
                "Please ensure that keyId, teamId and privateKey are provided in the additionalConfig"
            )

        payload = {
            "iss": config.additional_config.get("teamId"),
            "iat": time(),
            "exp": time() + (86400 * 180),  # 6 months
            "aud": "https://appleid.apple.com",
            "sub": get_actual_client_id_from_development_client_id(config.client_id),
        }
        headers = {"kid": config.additional_config.get("keyId")}
        return encode(  # type: ignore
            payload,
            sub(r"\\n", "\n", config.additional_config.get("privateKey")),  # type: ignore
            algorithm="ES256",
            headers=headers,
        )  # type: ignore


def Apple(input: ProviderInput) -> Provider:
    if input.config.name is None:
        input.config.name = "Apple"

    if input.config.oidc_discovery_endpoint is None:
        input.config.oidc_discovery_endpoint = "https://appleid.apple.com/"

    input.config.authorization_endpoint_query_params = {
        "response_mode": "form_post",
        **(input.config.authorization_endpoint_query_params or {}),
    }

    return NewProvider(input, AppleImpl)
