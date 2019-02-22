"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Ambari Agent

  The following file from the Ambari 2.6 branch titan service was used as a template:
  https://github.com/apache/ambari/blob/branch-2.6/ambari-server/src/main/resources/common-services/TITAN/1.0.0/scripts/titan_client.py
"""

import sys
import os
from resource_management import *
from resource_management.libraries.functions import conf_select
from resource_management.libraries.functions import stack_select
from resource_management.libraries.functions import StackFeature
from resource_management.libraries.functions.stack_features import check_stack_feature
import janusgraph

from ambari_commons.os_family_impl import OsFamilyFuncImpl, OsFamilyImpl

class JanusGraphClient(Script):
    def get_component_name(self):
        return "janusgraph-client"

    def configure(self, env):
        import params
        env.set_params(params)
        janusgraph.janusgraph()

    def status(self, env):
        raise ClientComponentHasNoStatus()

@OsFamilyImpl(os_family=OsFamilyImpl.DEFAULT)
class JanusGraphClientLinux(JanusGraphClient):

    def pre_rolling_restart(self, env):
        import params
        env.set_params(params)

        if params.version and check_stack_feature(StackFeature.ROLLING_UPGRADE, params.version):
            conf_select.select(params.stack_name, "janusgraph", params.version)
            stack_select.select("janusgraph-client", params.version)

    def install(self, env):
        self.install_packages(env)
        self.configure(env)

if __name__ == "__main__":
    JanusGraphClient().execute()