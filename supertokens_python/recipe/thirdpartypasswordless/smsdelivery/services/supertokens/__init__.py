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


from typing import Any, Dict

from supertokens_python.ingredients.smsdelivery.services.supertokens import \
    SupertokensServiceConfig
from supertokens_python.ingredients.smsdelivery.types import \
    SMSDeliveryInterface
from supertokens_python.recipe.passwordless.smsdelivery.services.supertokens import \
    SuperTokensService as PlessSuperTokensService

from ....types import TypeThirdPartyPasswordlessSmsDeliveryInput


class SuperTokensService(SMSDeliveryInterface[TypeThirdPartyPasswordlessSmsDeliveryInput]):
    pless_supertokens_service: PlessSuperTokensService

    def __init__(self, config: SupertokensServiceConfig) -> None:
        self.pless_supertokens_service = PlessSuperTokensService(config)

    async def send_sms(self, input_: TypeThirdPartyPasswordlessSmsDeliveryInput, user_context: Dict[str, Any]) -> None:
        await self.pless_supertokens_service.send_sms(input_, user_context)
