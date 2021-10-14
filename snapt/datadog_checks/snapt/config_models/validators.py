# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

def initialize_instance(values, **kwargs):
    if 'url' not in values:
        raise ValueError('Field `url` is required')

    return values
