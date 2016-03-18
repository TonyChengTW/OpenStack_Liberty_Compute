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

from ceilometer.hardware import plugin
from ceilometer.hardware.pollsters import util
from ceilometer import sample


class _Base(plugin.HardwarePollster):

    CACHE_KEY = 'network'

    def generate_one_sample(self, host, c_data):
        value, metadata, extra = c_data
        return util.make_sample_from_host(host,
                                          name=self.IDENTIFIER,
                                          sample_type=sample.TYPE_CUMULATIVE,
                                          unit='datagrams',
                                          volume=value,
                                          res_metadata=metadata,
                                          extra=extra)


class NetworkAggregatedIPOutRequests(_Base):
    IDENTIFIER = 'network.ip.outgoing.datagrams'


class NetworkAggregatedIPInReceives(_Base):
    IDENTIFIER = 'network.ip.incoming.datagrams'
