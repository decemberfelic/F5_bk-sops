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

__group_name__ = _(u"F5负载均衡(LTM)")
__group_icon__ = '%scomponents/atoms/sites/%s/f5/logo.png' % (settings.STATIC_URL, settings.RUN_VER)


class F5poolCustomService(Service):

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        supplier_account = parent_data.get_one_of_inputs('biz_supplier_account')

        name = data.get_one_of_inputs('pool_value1')
        monitor = data.get_one_of_inputs('pool_value2')
        members = data.get_one_of_inputs('pool_value3')

        client = get_client_by_user('admin')
        kwargs = {
            'api_path': "/mgmt/tm/ltm/pool/",
            "api_method": "POST",
            "params": {
                'name': name,
                'monitor': monitor,

                "members": members,
            },
            "auth_params": {
                "username": "admin",
                "password": "adtec@123",
                "loginProviderName": "tmos"
            }
        }
        result = client.f5_bigip.ltm(kwargs)

        if not result['result']:
            data.set_outputs('name', result['name'])
            return True
        else:
            data.set_outputs('ex_data', result['message'])
            return False

    def outputs_format(self):

        return [
            self.OutputItem(name=u'Pool名称：', key='name', type='str'),
        ]


class F5poolCustomComponent(Component):
    name = _(u"创建Pool")
    code = 'f5_pool'
    bound_service = F5poolCustomService
    form = '%scomponents/atoms/sites/%s/f5/f5_pool.js' % (settings.STATIC_URL, settings.RUN_VER)


class F5vsCustomService(Service):

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        supplier_account = parent_data.get_one_of_inputs('biz_supplier_account')

        name = data.get_one_of_inputs('vs_value1')
        destination = data.get_one_of_inputs('vs_value2')
        ipProtocol = data.get_one_of_inputs('vs_value3')
        pool = data.get_one_of_inputs('vs_value4')
        profiles = data.get_one_of_inputs('vs_value5')

        client = get_client_by_user('admin')
        kwargs = {
            'api_path': "/mgmt/tm/ltm/virtual/",
            "api_method": "POST",
            "params": {
                'name': name,
                'destination': destination,
                "ipProtocol": ipProtocol,
                "pool": pool,
                "sourceAddressTranslation": {"type": "automap"},
                "profiles": profiles
            },
            "auth_params": {
                "username": "admin",
                "password": "adtec@123",
                "loginProviderName": "tmos"
            }
        }
        result = client.f5_bigip.ltm(kwargs)
        if not result['result']:
            data.set_outputs('name', result['name'])
            return True
        else:
            data.set_outputs('ex_data', result['message'])
            return False

    def outputs_format(self):
        return [
            self.OutputItem(name=u'Pool名称：', key='name', type='str'),
        ]


class F5vsCustomComponent(Component):
    name = _(u"创建VS")
    code = 'f5_vs'
    bound_service = F5vsCustomService
    form = '%scomponents/atoms/sites/%s/f5/f5_vs.js' % (settings.STATIC_URL, settings.RUN_VER)


class F5monitorCustomService(Service):

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        supplier_account = parent_data.get_one_of_inputs('biz_supplier_account')

        name = data.get_one_of_inputs('health_value1')

        client = get_client_by_user('admin')
        kwargs = {
            'api_path': "/mgmt/tm/ltm/monitor/http/",
            "api_method": "POST",
            "params": {
                'name': name,
                'send': "GET / HTTP/1.0\r\n\r\n",
                "recv": "",
            },
            "auth_params": {
                "username": "admin",
                "password": "adtec@123",
                "loginProviderName": "tmos"
            }
        }
        result = client.f5_bigip.ltm(kwargs)

        if not result['result']:
            data.set_outputs('name', result['name'])
            return True
        else:
            data.set_outputs('ex_data', result['message'])
            return False

    def outputs_format(self):
        return [
            self.OutputItem(name=u'Pool名称：', key='name', type='str'),
        ]


class F5monitorCustomComponent(Component):
    name = _(u"健康检查")
    code = 'f5_monitor'
    bound_service = F5monitorCustomService
    form = '%scomponents/atoms/sites/%s/f5/f5_monitor.js' % (settings.STATIC_URL, settings.RUN_VER)


class F5profileCustomService(Service):

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        supplier_account = parent_data.get_one_of_inputs('biz_supplier_account')

        name = data.get_one_of_inputs('profile_value1')

        client = get_client_by_user('admin')
        kwargs = {
            'api_path': "/mgmt/tm/ltm/profile/http/",
            "api_method": "POST",
            "params": {
                'name': name,
                'insertXforwardedFor': "enabled",
            },
            "auth_params": {
                "username": "admin",
                "password": "adtec@123",
                "loginProviderName": "tmos"
            }
        }
        result = client.f5_bigip.ltm(kwargs)

        if not result['result']:
            data.set_outputs('name', result['name'])
            return True
        else:
            data.set_outputs('ex_data', result['message'])
            return False

    def outputs_format(self):
        return [
            self.OutputItem(name=u'Pool名称：', key='name', type='str'),
        ]


class F5profileCustomComponent(Component):
    name = _(u"profile")
    code = 'f5_profile'
    bound_service = F5profileCustomService
    form = '%scomponents/atoms/sites/%s/f5/f5_profile.js' % (settings.STATIC_URL, settings.RUN_VER)


class F5vsStatusCustomService(Service):

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        supplier_account = parent_data.get_one_of_inputs('biz_supplier_account')

       # name = data.get_one_of_inputs('vs_status1')

        client = get_client_by_user('admin')
        kwargs = {
            'api_path': "/mgmt/tm/ltm/pool",
            "api_method": "POST",
            "params": {

            },
            "auth_params": {
                "username": "admin",
                "password": "adtec@123",
                "loginProviderName": "tmos"
            }
        }
        result = client.f5_bigip.ltm(kwargs)
        if not result['result']:
            data.set_outputs('name', result['name'])
            return True
        else:
            data.set_outputs('ex_data', result['message'])
            return False

    def outputs_format(self):
        return [
            self.OutputItem(name=u'Pool名称：', key='name', type='str'),
        ]


class F5vsStatusCustomComponent(Component):
    name = _(u"业务查看")
    code = 'f5_vsstatus'
    bound_service = F5vsStatusCustomService
    form = '%scomponents/atoms/sites/%s/f5/f5_vs_status.js' % (settings.STATIC_URL, settings.RUN_VER)
