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

from supertokens_python.normalised_url_domain import NormalisedURLDomain
from supertokens_python.normalised_url_path import NormalisedURLPath
from tests.utils import (
    reset, setup_st, clean_st
)


def setup_function(f):
    reset()
    clean_st()
    setup_st()


def teardown_function(f):
    reset()
    clean_st()


def testing_URL_path_normalisation():

    def normalise_url_path_or_throw_error(input: str):
        return NormalisedURLPath(input).get_as_string_dangerous()

    assert normalise_url_path_or_throw_error("exists?email=john.doe%40gmail.com") == "/exists"
    assert normalise_url_path_or_throw_error("/auth/email/exists?email=john.doe%40gmail.com") == "/auth/email/exists"
    assert normalise_url_path_or_throw_error("exists") == "/exists"
    assert normalise_url_path_or_throw_error("/exists") == "/exists"
    assert normalise_url_path_or_throw_error("/exists?email=john.doe%40gmail.com") == "/exists"
    assert normalise_url_path_or_throw_error("http://api.example.com") == ""
    assert normalise_url_path_or_throw_error("https://api.example.com") == ""
    assert normalise_url_path_or_throw_error("http://api.example.com?hello=1") == ""
    assert normalise_url_path_or_throw_error("http://api.example.com/hello") == "/hello"
    assert normalise_url_path_or_throw_error("http://api.example.com/") == ""
    assert normalise_url_path_or_throw_error("http://api.example.com:8080") == ""
    assert normalise_url_path_or_throw_error("api.example.com/") == ""
    assert normalise_url_path_or_throw_error("api.example.com#random") == ""
    assert normalise_url_path_or_throw_error(".example.com") == ""
    assert normalise_url_path_or_throw_error("api.example.com/?hello=1&bye=2") == ""

    assert normalise_url_path_or_throw_error("http://api.example.com/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("http://1.2.3.4/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("1.2.3.4/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("https://api.example.com/one/two/") == "/one/two"
    assert normalise_url_path_or_throw_error("http://api.example.com/one/two?hello=1") == "/one/two"
    assert normalise_url_path_or_throw_error("http://api.example.com/hello/") == "/hello"
    assert normalise_url_path_or_throw_error("http://api.example.com/one/two/") == "/one/two"
    assert normalise_url_path_or_throw_error("http://api.example.com/one/two#random2") == "/one/two"
    assert normalise_url_path_or_throw_error("api.example.com/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error(".example.com/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("api.example.com/one/two?hello=1&bye=2") == "/one/two"

    assert normalise_url_path_or_throw_error("/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("one/two/") == "/one/two"
    assert normalise_url_path_or_throw_error("/one") == "/one"
    assert normalise_url_path_or_throw_error("one") == "/one"
    assert normalise_url_path_or_throw_error("one/") == "/one"
    assert normalise_url_path_or_throw_error("/one/two/") == "/one/two"
    assert normalise_url_path_or_throw_error("/one/two?hello=1") == "/one/two"
    assert normalise_url_path_or_throw_error("one/two?hello=1") == "/one/two"
    assert normalise_url_path_or_throw_error("/one/two/#randm,") == "/one/two"
    assert normalise_url_path_or_throw_error("one/two#random") == "/one/two"

    assert normalise_url_path_or_throw_error("localhost:4000/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("127.0.0.1:4000/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("127.0.0.1/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("https://127.0.0.1:80/one/two") == "/one/two"
    assert normalise_url_path_or_throw_error("/") == ""
    assert normalise_url_path_or_throw_error("") == ""

    assert normalise_url_path_or_throw_error("/.netlify/functions/api") == "/.netlify/functions/api"
    assert normalise_url_path_or_throw_error("/netlify/.functions/api") == "/netlify/.functions/api"
    assert normalise_url_path_or_throw_error("app.example.com/.netlify/functions/api") == "/.netlify/functions/api"
    assert normalise_url_path_or_throw_error("app.example.com/netlify/.functions/api") == "/netlify/.functions/api"
    assert normalise_url_path_or_throw_error("/app.example.com") == "/app.example.com"


def testing_URL_domain_normalisation():

    def normalise_url_domain_or_throw_error(input: str):
        return NormalisedURLDomain(input).get_as_string_dangerous()

    assert normalise_url_domain_or_throw_error("http://api.example.com") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("https://api.example.com") == "https://api.example.com"
    assert normalise_url_domain_or_throw_error("http://api.example.com?hello=1") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("http://api.example.com/hello") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("http://api.example.com/") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("http://api.example.com#random2") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("http://api.example.com:8080") == "http://api.example.com:8080"
    assert normalise_url_domain_or_throw_error("api.example.com/") == "https://api.example.com"
    assert normalise_url_domain_or_throw_error("api.example.com") == "https://api.example.com"
    assert normalise_url_domain_or_throw_error("api.example.com#random") == "https://api.example.com"
    assert normalise_url_domain_or_throw_error(".example.com") == "https://example.com"
    assert normalise_url_domain_or_throw_error("api.example.com/?hello=1&bye=2") == "https://api.example.com"
    assert normalise_url_domain_or_throw_error("localhost") == "http://localhost"
    assert normalise_url_domain_or_throw_error("https://localhost") == "https://localhost"

    assert normalise_url_domain_or_throw_error("http://api.example.com/one/two") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("http://1.2.3.4/one/two") == "http://1.2.3.4"
    assert normalise_url_domain_or_throw_error("https://1.2.3.4/one/two") == "https://1.2.3.4"
    assert normalise_url_domain_or_throw_error("1.2.3.4/one/two") == "http://1.2.3.4"
    assert normalise_url_domain_or_throw_error("https://api.example.com/one/two/") == "https://api.example.com"
    assert normalise_url_domain_or_throw_error("http://api.example.com/one/two?hello=1") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("http://api.example.com/one/two#random2") == "http://api.example.com"
    assert normalise_url_domain_or_throw_error("api.example.com/one/two") == "https://api.example.com"
    assert normalise_url_domain_or_throw_error(".example.com/one/two") == "https://example.com"
    assert normalise_url_domain_or_throw_error("localhost:4000") == "http://localhost:4000"
    assert normalise_url_domain_or_throw_error("127.0.0.1:4000") == "http://127.0.0.1:4000"
    assert normalise_url_domain_or_throw_error("127.0.0.1") == "http://127.0.0.1"
    assert normalise_url_domain_or_throw_error("https://127.0.0.1:80/") == "https://127.0.0.1:80"

    try:
        normalise_url_domain_or_throw_error("/one/two")
    except Exception as e:
        assert str(e) == 'Please provide a valid domain name'

    try:
        normalise_url_domain_or_throw_error("/.netlify/functions/api")
    except Exception as e:
        assert str(e) == 'Please provide a valid domain name'


def testing_override_test():
    m = None

    class OI:
        def __init__(self):
            pass

        def some_other_func(self):
            nonlocal m
            m = 1

        def some_func(self):
            self.some_other_func()

    class A(OI):
        def __init__(self):
            super().__init__()

        def some_other_func(self):
            nonlocal m
            m = 2

    b = A()

    def some_other_func():
        nonlocal m
        m = 4

    b.some_other_func = some_other_func

    b.some_func()

    assert m == 4


def testing_super_recipe_tests():
    m = 0

    class EP:
        def __init__(self):
            pass

        def sign_up(self):
            self.get_user()

        def get_user(self):
            nonlocal m
            m = 1

    class TPEP:
        def __init__(self):
            ep = EP()
            self.o_sign_up = ep.sign_up
            self.o_get_user = ep.get_user
            dep = DerivedEP(self)
            ep.sign_up = dep.sign_up
            ep.get_user = dep.get_user

        def sign_up(self):
            self.o_sign_up()

        def get_users(self):
            self.o_get_user()

    class DerivedEP(EP):
        def __init__(self, tpep):
            super().__init__()
            self.tpep = tpep

        def sign_up(self):
            self.tpep.sign_up()

        def get_user(self):
            self.tpep.get_users()

    def override(tpep):
        o_sign_up = tpep.sign_up
        o_get_users = tpep.get_users

        def sign_up():
            o_sign_up()

        def get_users():
            nonlocal m
            m = 5
            o_get_users()
            if m == 1:
                m = 2

        tpep.sign_up = sign_up
        tpep.get_users = get_users
        return tpep

    base_tpep = TPEP()

    override_tpep = override(base_tpep)

    override_tpep.sign_up()
    assert m == 2

    m = 1
    ep = DerivedEP(override_tpep)

    ep.get_user()

    assert m == 2