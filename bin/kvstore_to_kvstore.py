import ta_synckvstore_declare

import os
import sys
import time
import datetime

import modinput_wrapper.base_modinput
from solnlib.packages.splunklib import modularinput as smi



import input_module_kvstore_to_kvstore as input_module


'''
    Do not edit this file!!!
    This file is generated by Add-on builder automatically.
    Add your modular input logic to file input_module_kvstore_to_kvstore.py
'''
class ModInputkvstore_to_kvstore(modinput_wrapper.base_modinput.BaseModInput):

    def __init__(self):
        if 'use_single_instance_mode' in dir(input_module):
            use_single_instance = input_module.use_single_instance_mode()
        else:
            use_single_instance = False
        super(ModInputkvstore_to_kvstore, self).__init__("ta_synckvstore", "kvstore_to_kvstore", use_single_instance)
        self.global_checkbox_fields = None

    def get_scheme(self):
        """overloaded splunklib modularinput method"""
        scheme = super(ModInputkvstore_to_kvstore, self).get_scheme()
        scheme.title = ("KVStore to KVStore")
        scheme.description = ("Modular Input to pull Remote KVStore table to a Local KVstore table")
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True

        scheme.add_argument(smi.Argument("name", title="Name",
                                         description="",
                                         required_on_create=True))

        """
        For customized inputs, hard code the arguments here to hide argument detail from users.
        For other input types, arguments should be get from input_module. Defining new input types could be easier.
        """
        scheme.add_argument(smi.Argument("u_splunkserver", title="Splunk Server",
                                         description="The Remote Splunk Server with the source KVStore",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("u_srcapp", title="Source App",
                                         description="The remote app context with the source KVStore Collection",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("u_srccollection", title="Source Collection",
                                         description="The remote source KVStore Collection Name",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("global_account", title="Global Account",
                                         description="The stored rest API credential valid on the remote Splunk Server with permissions to the source KVStore",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("u_desttableaction", title="Destination Table Action",
                                         description="Choose to force destination table full replacement or update table.",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("u_destapp", title="Destination App",
                                         description="The local app context with the destination KVStore Collection",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("u_destcollection", title="Destination Collection",
                                         description="The local destination KVStore Collection Name",
                                         required_on_create=True,
                                         required_on_edit=False))
        return scheme

    def get_app_name(self):
        return "TA-SyncKVStore"

    def validate_input(self, definition):
        """validate the input stanza"""
        input_module.validate_input(self, definition)

    def collect_events(self, ew):
        """write out the events"""
        input_module.collect_events(self, ew)

    def get_account_fields(self):
        account_fields = []
        account_fields.append("global_account")
        return account_fields

    def get_checkbox_fields(self):
        checkbox_fields = []
        return checkbox_fields

    def get_global_checkbox_fields(self):
        if self.global_checkbox_fields is None:
            checkbox_fields = []
            customized_settings = {u'customized_options': [{u'name': u'u_splunkserver', u'value': u''}, {u'name': u'u_srcapp', u'value': u''}, {u'name': u'u_srccollection', u'value': u''}, {u'name': u'global_account', u'value': u''}, {u'name': u'u_desttableaction', u'value': u'replace'}, {u'name': u'u_destapp', u'value': u''}, {u'name': u'u_destcollection', u'value': u''}], u'code': u'\n# encoding = utf-8\n\nimport os\nimport sys\nimport time\nimport datetime\n\n\'\'\'\n    IMPORTANT\n    Edit only the validate_input and collect_events functions.\n    Do not edit any other part in this file.\n    This file is generated only once when creating the modular input.\n\'\'\'\n\'\'\'\n# For advanced users, if you want to create single instance mod input, uncomment this method.\ndef use_single_instance_mode():\n    return True\n\'\'\'\n\ndef validate_input(helper, definition):\n    """Implement your own validation logic to validate the input stanza configurations"""\n    # This example accesses the modular input variable\n    # global_account = definition.parameters.get(\'global_account\', None)\n    pass\n\ndef collect_events(helper, ew):\n    """Implement your data collection logic here\n\n    # The following examples get the arguments of this input.\n    # Note, for single instance mod input, args will be returned as a dict.\n    # For multi instance mod input, args will be returned as a single value.\n    opt_global_account = helper.get_arg(\'global_account\')\n    # In single instance mode, to get arguments of a particular input, use\n    opt_global_account = helper.get_arg(\'global_account\', stanza_name)\n\n    # get input type\n    helper.get_input_type()\n\n    # The following examples get input stanzas.\n    # get all detailed input stanzas\n    helper.get_input_stanza()\n    # get specific input stanza with stanza name\n    helper.get_input_stanza(stanza_name)\n    # get all stanza names\n    helper.get_input_stanza_names()\n\n    # The following examples get options from setup page configuration.\n    # get the loglevel from the setup page\n    loglevel = helper.get_log_level()\n    # get proxy setting configuration\n    proxy_settings = helper.get_proxy()\n    # get account credentials as dictionary\n    account = helper.get_user_credential_by_username("username")\n    account = helper.get_user_credential_by_id("account id")\n    # get global variable configuration\n    global_userdefined_global_var = helper.get_global_setting("userdefined_global_var")\n\n    # The following examples show usage of logging related helper functions.\n    # write to the log for this modular input using configured global log level or INFO as default\n    helper.log("log message")\n    # write to the log using specified log level\n    helper.log_debug("log message")\n    helper.log_info("log message")\n    helper.log_warning("log message")\n    helper.log_error("log message")\n    helper.log_critical("log message")\n    # set the log level for this modular input\n    # (log_level can be "debug", "info", "warning", "error" or "critical", case insensitive)\n    helper.set_log_level(log_level)\n\n    # The following examples send rest requests to some endpoint.\n    response = helper.send_http_request(url, method, parameters=None, payload=None,\n                                        headers=None, cookies=None, verify=True, cert=None,\n                                        timeout=None, use_proxy=True)\n    # get the response headers\n    r_headers = response.headers\n    # get the response body as text\n    r_text = response.text\n    # get response body as json. If the body text is not a json string, raise a ValueError\n    r_json = response.json()\n    # get response cookies\n    r_cookies = response.cookies\n    # get redirect history\n    historical_responses = response.history\n    # get response status code\n    r_status = response.status_code\n    # check the response status, if the status is not sucessful, raise requests.HTTPError\n    response.raise_for_status()\n\n    # The following examples show usage of check pointing related helper functions.\n    # save checkpoint\n    helper.save_check_point(key, state)\n    # delete checkpoint\n    helper.delete_check_point(key)\n    # get checkpoint\n    state = helper.get_check_point(key)\n\n    # To create a splunk event\n    helper.new_event(data, time=None, host=None, index=None, source=None, sourcetype=None, done=True, unbroken=True)\n    """\n\n    \'\'\'\n    # The following example writes a random number as an event. (Multi Instance Mode)\n    # Use this code template by default.\n    import random\n    data = str(random.randint(0,100))\n    event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data)\n    ew.write_event(event)\n    \'\'\'\n\n    \'\'\'\n    # The following example writes a random number as an event for each input config. (Single Instance Mode)\n    # For advanced users, if you want to create single instance mod input, please use this code template.\n    # Also, you need to uncomment use_single_instance_mode() above.\n    import random\n    input_type = helper.get_input_type()\n    for stanza_name in helper.get_input_stanza_names():\n        data = str(random.randint(0,100))\n        event = helper.new_event(source=input_type, index=helper.get_output_index(stanza_name), sourcetype=helper.get_sourcetype(stanza_name), data=data)\n        ew.write_event(event)\n    \'\'\'\n    \n    try:\n        import splunklib.client as splunkClient\n        import json\n        import requests\n        import threading, Queue\n    except Exception as err_message:\n        helper.log_error("{}".format(err_message))\n        return 1\n\n    _max_content_bytes = 100000\n    _max_content_records = 1000\n    _number_of_threads = 5\n    _splunk_server_verify = False\n\n    # Define my own class to put data into KVStore. \n    # The Splunk Python SDK is not threaded for KVStore operations\n    class splunk_sendto_kvstore:\n\n        def __init__(self, splunk_server, splunk_app, splunk_collection, session_key):\n            self.splunk_server = splunk_server\n            self.splunk_app = splunk_app\n            self.splunk_collection = splunk_collection\n            self.session_key = session_key\n            self.flushQueue = Queue.Queue(0)\n            for x in range(_number_of_threads):\n                t = threading.Thread(target=self.batchThread)\n                t.daemon = True\n                t.start()\n\n        def postDataToSplunk(self, data):\n            self.flushQueue.put(data)\n        \n        def batchThread(self):\n            while True:\n                data = self.flushQueue.get()\n                headers = {\'Content-type\': \'application/json\', \'Accept\': \'text/plain\', \'Authorization\':\'Splunk {}\'.format(self.session_key)}\n                splunk_url = \'\'.join([\'https://\',self.splunk_server,\':8089/servicesNS/nobody/\',self.splunk_app,\'/storage/collections/data/\',self.splunk_collection,\'/\',\'batch_save\'])\n                payload_length = sum(len(json.dumps(item)) for item in data)\n                r = requests.post(splunk_url,verify=_splunk_server_verify,headers=headers,data=json.dumps(data))\n                if not r.status_code == requests.codes.ok:\n                    helper.log_error("{}".format(r.text))\n                self.flushQueue.task_done()\n\n        def waitUntilDone(self):\n            self.flushQueue.join()\n            return\n   \n    helper.log_info("Modular Input pullkvtokv started.")\n\n    u_session_key = helper.context_meta.get(\'session_key\')\n    \n    u_splunkserver = helper.get_arg(\'u_splunkserver\')\n    helper.log_info("u_splunkserver={}".format(u_splunkserver))\n\n    u_srcappname = helper.get_arg("u_srcapp")\n    helper.log_info("u_destappname={}".format(u_srcappname))\n\n    u_srccollection = helper.get_arg("u_srccollection")\n    helper.log_info("u_destcollection={}".format(u_srccollection))\n    \n    u_destappname = helper.get_arg("u_destapp")\n    helper.log_info("u_destappname={}".format(u_destappname))\n\n    u_destcollection = helper.get_arg("u_destcollection")\n    helper.log_info("u_destcollection={}".format(u_destcollection))\n    \n    u_desttableaction = helper.get_arg("u_desttableaction")\n    helper.log_info("u_desttableaction={}".format(u_desttableaction))\n    \n    user_account = helper.get_arg(\'global_account\')\n    if not user_account:\n        helper.log_error("No user account selected")\n        return 1\n    \n    srcSplunkService = splunkClient.connect(host=u_splunkserver, port=8089, username=user_account.get(\'username\'), password=user_account.get(\'password\'),owner=\'nobody\',app=u_srcappname)\n    \n    srcKVStoreTable = srcSplunkService.kvstore[u_srccollection].data.query()\n    \n    destSplunkService = splunkClient.connect(token=u_session_key, owner=\'nobody\', app=u_destappname)\n    \n    #Check if KVStore collection exists\n    if u_destcollection not in destSplunkService.kvstore:\n        helper.log_error("KVStore collection {0} not on local Splunk instance".format(u_destcollection))\n        return 1\n   \n    # If replace method is selected use SDK KVStore to delete the data in the collection\n    if u_desttableaction == "replace":\n        destSplunkService.kvstore[u_destcollection].data.delete()\n        helper.log_info("action=deleted collection_name={0} message=\\"Remote Collection Data Deleted\\"".format(u_destcollection))\n\n    # Define our threaded class for KVStore data submission        \n    destKVStore = splunk_sendto_kvstore(\'localhost\', u_destappname, u_destcollection, u_session_key)\n    \n    postList = []\n    for entry in srcKVStoreTable:\n        if ((len(json.dumps(postList)) + len(json.dumps(entry))) < _max_content_bytes) and (len(postList) + 1 < _max_content_records):\n            postList.append(entry)\n        else:\n            destKVStore.postDataToSplunk(postList)\n            postList = []\n            postList.append(entry)\n            \n    destKVStore.postDataToSplunk(postList)\n        \n    destKVStore.waitUntilDone()\n    \n    helper.log_info("Modular Input pullkvtokv completed.")\n\n\n', u'is_loaded': True, u'data_inputs_options': [{u'required_on_create': True, u'default_value': u'', u'title': u'Splunk Server', u'description': u'The Remote Splunk Server with the source KVStore', u'placeholder': u'', u'required_on_edit': False, u'format_type': u'text', u'name': u'u_splunkserver', u'type': u'customized_var'}, {u'required_on_create': True, u'default_value': u'', u'title': u'Source App', u'description': u'The remote app context with the source KVStore Collection', u'placeholder': u'', u'required_on_edit': False, u'format_type': u'text', u'name': u'u_srcapp', u'type': u'customized_var'}, {u'required_on_create': True, u'default_value': u'', u'title': u'Source Collection', u'description': u'The remote source KVStore Collection Name', u'placeholder': u'', u'required_on_edit': False, u'format_type': u'text', u'name': u'u_srccollection', u'type': u'customized_var'}, {u'required_on_create': True, u'default_value': u'', u'title': u'Global Account', u'description': u'The stored rest API credential valid on the remote Splunk Server with permissions to the source KVStore', u'placeholder': u'', u'required_on_edit': False, u'format_type': u'global_account', u'name': u'global_account', u'type': u'customized_var', u'possible_values': []}, {u'required_on_create': True, u'default_value': u'update', u'title': u'Destination Table Action', u'description': u'Choose to force destination table full replacement or update table.', u'required_on_edit': False, u'format_type': u'radiogroup', u'name': u'u_desttableaction', u'type': u'customized_var', u'possible_values': [{u'value': u'replace', u'label': u'Replace Table'}, {u'value': u'update', u'label': u'Update Table'}]}, {u'required_on_create': True, u'default_value': u'', u'title': u'Destination App', u'description': u'The local app context with the destination KVStore Collection', u'placeholder': u'', u'required_on_edit': False, u'format_type': u'text', u'name': u'u_destapp', u'type': u'customized_var'}, {u'required_on_create': True, u'default_value': u'', u'title': u'Destination Collection', u'description': u'The local destination KVStore Collection Name', u'placeholder': u'', u'required_on_edit': False, u'format_type': u'text', u'name': u'u_destcollection', u'type': u'customized_var'}], u'disabled': True, u'type': u'customized', 'index': u'default', u'title': u'KVStore to KVStore', u'name': u'kvstore_to_kvstore', 'streaming_mode_xml': True, 'interval': u'120', u'description': u'Modular Input to pull Remote KVStore table to a Local KVstore table', u'sample_count': 0, u'uuid': u'14a5c6a397354f59b30efcd195335e18', u'parameters': [{u'default_value': u'', u'help_string': u'The Remote Splunk Server with the source KVStore', u'name': u'u_splunkserver', u'required': True, u'value': u'', u'placeholder': u'', u'format_type': u'text', u'type': u'text', u'label': u'Splunk Server'}, {u'default_value': u'', u'help_string': u'The remote app context with the source KVStore Collection', u'name': u'u_srcapp', u'required': True, u'value': u'', u'placeholder': u'', u'format_type': u'text', u'type': u'text', u'label': u'Source App'}, {u'default_value': u'', u'help_string': u'The remote source KVStore Collection Name', u'name': u'u_srccollection', u'required': True, u'value': u'', u'placeholder': u'', u'format_type': u'text', u'type': u'text', u'label': u'Source Collection'}, {u'default_value': u'', u'help_string': u'The stored rest API credential valid on the remote Splunk Server with permissions to the source KVStore', u'name': u'global_account', u'possible_values': [], u'value': u'', u'placeholder': u'', u'format_type': u'global_account', u'required': True, u'type': u'global_account', u'label': u'Global Account'}, {u'default_value': u'update', u'name': u'u_desttableaction', u'possible_values': [{u'value': u'replace', u'label': u'Replace Table'}, {u'value': u'update', u'label': u'Update Table'}], u'value': u'replace', u'help_string': u'Choose to force destination table full replacement or update table.', u'format_type': u'radiogroup', u'required': True, u'type': u'radiogroup', u'label': u'Destination Table Action'}, {u'default_value': u'', u'help_string': u'The local app context with the destination KVStore Collection', u'name': u'u_destapp', u'required': True, u'value': u'', u'placeholder': u'', u'format_type': u'text', u'type': u'text', u'label': u'Destination App'}, {u'default_value': u'', u'help_string': u'The local destination KVStore Collection Name', u'name': u'u_destcollection', u'required': True, u'value': u'', u'placeholder': u'', u'format_type': u'text', u'type': u'text', u'label': u'Destination Collection'}], 'use_external_validation': True, 'sourcetype': u'kv2kv'}.get('global_settings', {}).get('customized_settings', [])
            for global_var in customized_settings:
                if global_var.get('type', '') == 'checkbox':
                    checkbox_fields.append(global_var['name'])
            self.global_checkbox_fields = checkbox_fields
        return self.global_checkbox_fields

if __name__ == "__main__":
    exitcode = ModInputkvstore_to_kvstore().run(sys.argv)
    sys.exit(exitcode)
