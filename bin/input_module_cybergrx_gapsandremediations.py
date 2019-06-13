# encoding = utf-8

import os
import sys
import time
import json
import datetime
'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''
'''
# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''


def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # grx_api_token = definition.parameters.get('grx_api_token', None)
    pass


def collect_events(helper, ew):
    helper.set_log_level("DEBUG")

    global_cybergrx_api = helper.get_global_setting("cybergrx_api") or "https://api.cybergrx.com/"
    global_cybergrx_api = global_cybergrx_api.rstrip("/")
    opt_grx_api_token = helper.get_arg('api_token').strip()

    proxy_settings = helper.get_proxy()

    url = "/v1/third-parties?limit=50"
    method = "GET"
    headers = {
        "Authorization": opt_grx_api_token,
        "Accept": "Application/json",
    }

    while url:
        response = helper.send_http_request(
            global_cybergrx_api + url, method, headers=headers, verify=True, use_proxy=True)

        # check the response status, if the status is not sucessful, raise requests.HTTPError
        response.raise_for_status()

        r_json = response.json()

        url = r_json.get('next', None)
        for company in r_json.get('items', []):
            residual_risk = company.get("residual_risk", [])
            if not residual_risk:
                continue

            report_uri = residual_risk[0].get("residual_risk_uri", None)
            if not report_uri:
                continue

            report_response = helper.send_http_request(
                global_cybergrx_api + report_uri, method, headers=headers, verify=True, use_proxy=True)

            # check the response status, if the status is not sucessful, raise requests.HTTPError
            report_response.raise_for_status()

            report_json = report_response.json()

            def emit_risk(risk, company):
                risk["question_id"] = risk["id"]
                risk["company_id"] = company["id"]
                risk["company_name"] = company["name"]
                risk["id"] = company["id"] + "-" + risk["number"]

                event = helper.new_event(
                    source=helper.get_input_type(),
                    index=helper.get_output_index(),
                    sourcetype=helper.get_sourcetype(),
                    data=json.dumps(risk))
                ew.write_event(event)

            for risk in report_json.get("high_risks", []):
                emit_risk(risk, company)

            for risk in report_json.get("medium_risks", []):
                emit_risk(risk, company)

            for risk in report_json.get("low_risks", []):
                emit_risk(risk, company)

            time.sleep(5)

        time.sleep(10)
