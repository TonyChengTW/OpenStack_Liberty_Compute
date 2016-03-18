# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.network import network_service
from openstack import resource


class SubnetPool(resource.Resource):
    resource_key = 'subnetpool'
    resources_key = 'subnetpools'
    base_path = '/subnetpools'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties
    #: The minimum prefix length that can be allocated from the
    #: subnet pool. *Type: int*
    minimum_prefix_length = resource.prop('min_prefixlen', type=int)
    #: The length of the prefix to allocate when the cidr or prefixlen
    #: attributes are omitted when creating a subnet. *Type: int*
    default_prefix_length = resource.prop('default_prefixlen', type=int)
    #: The maximum prefix length that can be allocated from the
    #: subnet pool. *Type: int*
    maximum_prefix_length = resource.prop('max_prefixlen', type=int)
    #: The subnet pool name.
    name = resource.prop('name')
    #: A per-project quota on the prefix space that can be allocated
    #: from the subnet pool for project subnets. For IPv4 subnet pools,
    #: default_quota is measured in units of /32. For IPv6 subnet pools,
    #: default_quota is measured units of /64. All projects that use the
    #: subnet pool have the same prefix quota applied. *Type: int*
    default_quota = resource.prop('default_quota', type=int)
    #: The ID of the project that owns the subnet pool.
    project_id = resource.prop('tenant_id')
    #: A list of subnet prefixes that are assigned to the subnet pool.
    #: The adjacent prefixes are merged and treated as a single prefix.
    #: *Type: list*
    prefixes = resource.prop('prefixes', type=list)
    #: Read-only. The IP address family of the list of prefixes.
    #: *Type: int*
    ip_version = resource.prop('ip_version', type=int)
    #: Indicates whether this subnet pool is shared across all projects.
    #: *Type: bool*
    is_shared = resource.prop('shared', type=bool)
