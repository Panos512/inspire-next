# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014, 2015 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Styleguide bundles."""

from invenio_ext.assets import Bundle

styles = Bundle(
    "less/styleguide.less",
    depends=[
        'less/inspire.less',
        'less/accounts/settings/account-settings.less',
        'less/base/variables.less',
        'less/base/header.less',
        'less/base/footer.less',
        'less/base/panels.less',
        'less/base/helpers.less',
        'less/base/sticky-footer.less',
        'less/base/list-group.less',
        'less/base/core.less',
        'less/accounts/login.less',
        'less/search/index.less',
        'less/feedback/button.less',
        'less/feedback/modal.less',
        'less/workflows/workflows.less',
    ],
    filters="less",
    output="custom.css",
    weight=91
)
