"""
Copyright (c) 2021, VRAI Labs and/or its affiliates. All rights reserved.

This software is licensed under the Apache License, Version 2.0 (the
"License") as published by the Apache Software Foundation.

You may not use this file except in compliance with the License. You may
obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""
from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from supertokens_python.framework.request import BaseRequest
    from supertokens_python.framework.response import BaseResponse
    from supertokens_python.emailpassword.recipe import EmailPasswordRecipe

from .utils import validate_form_fields_or_throw_error
from supertokens_python.emailpassword.constants import FORM_FIELD_PASSWORD_ID
from supertokens_python.utils import find_first_occurrence_in_list
from supertokens_python.exceptions import raise_bad_input_exception


async def handle_password_reset_api(recipe: EmailPasswordRecipe, request: BaseRequest):
    body = await request.json()
    form_fields_raw = body['formFields'] if 'formFields' in body else []
    form_fields = await validate_form_fields_or_throw_error(recipe,
                                                            recipe.config.reset_token_using_password_feature.form_fields_for_password_reset_form,
                                                            form_fields_raw)
    new_password = find_first_occurrence_in_list(lambda x: x.id == FORM_FIELD_PASSWORD_ID, form_fields).value
    if 'token' not in body:
        raise_bad_input_exception(recipe, 'Please provide the password reset token')
    if not isinstance(body['token'], str):
        raise_bad_input_exception(recipe, 'The password reset token must be a string')

    token = body['token']
    await recipe.reset_password_using_token(token, new_password)

    return BaseResponse(content={
        'status': 'OK'
    })
