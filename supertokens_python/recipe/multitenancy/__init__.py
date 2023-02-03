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

from typing import TYPE_CHECKING, Callable, Union
from supertokens_python import always_initialised_recipes

from . import exceptions as ex
from . import recipe

AllowedDomainsClaim = recipe.AllowedDomainsClaim
exceptions = ex

if TYPE_CHECKING:
    from supertokens_python.supertokens import AppInfo

    from ...recipe_module import RecipeModule
    from .interfaces import TypeGetTenantIdsForUserId, TypeGetAllowedDomainsForTenantId
    from .utils import InputErrorHandlers, InputOverrideConfig


def init(
    get_tenant_ids_for_user_id: Union[TypeGetTenantIdsForUserId, None] = None,
    get_allowed_domains_for_tenant_id: Union[
        TypeGetAllowedDomainsForTenantId, None
    ] = None,
    error_handlers: Union[InputErrorHandlers, None] = None,
    override: Union[InputOverrideConfig, None] = None,
) -> Callable[[AppInfo], RecipeModule]:
    return recipe.MultitenancyRecipe.init(
        get_tenant_ids_for_user_id,
        get_allowed_domains_for_tenant_id,
        error_handlers,
        override,
    )


always_initialised_recipes.DEFAULT_MULTITENANCY_RECIPE = init()
