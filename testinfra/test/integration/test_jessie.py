# -*- coding: utf8 -*-
# Copyright © 2015 Philippe Pepiot
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals

import pytest

pytestmark = pytest.mark.integration

hosts = ["debian_jessie"]


def test_ssh_package(Package):
    ssh = Package("openssh-server")
    assert ssh.is_installed
    assert ssh.version == "1:6.7p1-5"


def test_ssh_service(Service):
    ssh = Service("ssh")
    assert ssh.is_running
    assert ssh.is_enabled


def test_systeminfo(SystemInfo):
    assert SystemInfo.type == "linux"
    assert SystemInfo.release == "8.0"
    assert SystemInfo.distribution == "debian"
    assert SystemInfo.codename == "jessie"


def test_salt(Salt):
    assert Salt("pkg.version", "openssh-server", local=True) == "1:6.7p1-5"


def test_puppet_resource(PuppetResource):
    assert PuppetResource("package", "openssh-server") == {
        "openssh-server": {"ensure": "1:6.7p1-5"},
    }


def test_facter(Facter):
    assert Facter()["lsbdistcodename"] == "jessie"
    assert Facter("lsbdistcodename") == {
        "lsbdistcodename": "jessie",
    }