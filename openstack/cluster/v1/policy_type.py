# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.cluster import cluster_service
from openstack import resource


class PolicyType(resource.Resource):
    id_attribute = 'name'
    resource_key = 'policy_type'
    resources_key = 'policy_types'
    base_path = '/policy-types'
    service = cluster_service.ClusterService()

    # Capabilities
    allow_list = True
    allow_retrieve = True

    # Properties
    #: Name of policy type.
    name = resource.prop('name')
    #: The schema of the policy type.
    schema = resource.prop('schema')
