# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from .__about__ import __version__
from .balancer.haproxy import BalancerCheck
# from .accelerator.nginx import AcceleratorCheck
# from .metrics import VTS_METRIC_MAP


__all__ = [
    '__version__',
    'BalancerCheck',
    # 'AcceleratorCheck',
    # 'VTS_METRIC_MAP',
]
