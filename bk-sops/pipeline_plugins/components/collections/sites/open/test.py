# -*- coding: utf-8 -*-

import logging

from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component
from pipeline_plugins.components.utils import get_ip_by_regex, handle_api_error
from gcloud.conf import settings

logger = logging.getLogger('celery')
get_client_by_user = settings.ESB_GET_CLIENT_BY_USER

__group_name__ = _(u"测试原子(TEST)")
# __group_icon__ = '%scomponents/atoms/sites/%s/cc/cc.png' % (settings.STATIC_URL, settings.RUN_VER)


class TestCustomService(Service):

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        supplier_account = parent_data.get_one_of_inputs('biz_supplier_account')

        name = data.get_one_of_inputs('test_custom_value')
        recv = data.get_one_of_inputs('test_custom_value2')

        client = get_client_by_user('admin')
        kwargs = {
            'name': name,
            "sned": "GET / HTTP/1.0\r\n\r\n",
            "recv": recv
        }
        result = client.f5_bigip.ltm(kwargs)
        if result['xxxxxxx'] == 0:
            return True
        else:
            return False


    def outputs_format(self):
        return []


class TestCustomComponent(Component):
    name = _(u"测试原子")
    code = 'test_custom'
    bound_service = TestCustomService
    form = '%scomponents/atoms/sites/%s/test/test_custom.js' % (settings.STATIC_URL, settings.RUN_VER)

