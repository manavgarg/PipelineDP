# Copyright 2022 OpenMined.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from absl.testing import absltest
from absl.testing import parameterized

import pipeline_dp.sampling_utils as sampling_utils


class SamplingUtilsTest(parameterized.TestCase):

    def _check_is_subset(self, a: list, b: list) -> bool:
        return set(a).issubset(set(b))

    @parameterized.parameters({
        "size": 1,
        "sample_sizes": [1, 2, 10, 20]
    }, {
        "size": 10,
        "sample_sizes": [1, 2, 10, 20]
    })
    def test_choose_from_list_ints(self, size, sample_sizes):
        a = list(range(size))
        for sample_size in sample_sizes:
            sample = sampling_utils.choose_from_list_without_replacement(
                a, sample_size)
            self.assertTrue(self._check_is_subset(sample, a))

    @parameterized.parameters({
        "size": 1,
        "sample_sizes": [1, 2, 10, 20]
    }, {
        "size": 10,
        "sample_sizes": [1, 2, 10, 20]
    })
    def test_choose_from_list_tuples(self, size, sample_sizes):
        a = [(i, i) for i in range(size)]
        for sample_size in sample_sizes:
            sample = sampling_utils.choose_from_list_without_replacement(
                a, sample_size)
            self.assertTrue(self._check_is_subset(sample, a))


if __name__ == '__main__':
    absltest.main()
