@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################
    
    import http.client
    import json
    from urllib.parse import urlparse
    url = "https://webhook.site/xxxxxxxxxx Your web hook URL xxxxxxxxx"
    parsed_url = urlparse(url)

    conn = http.client.HTTPSConnection(parsed_url.hostname)

    payload = json.dumps({
        "container_id": container.get("id"),
        "name": container.get("name"),
        "label": container.get("label"),
        "message": "Test from custom code"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    conn.request("POST", parsed_url.path, body=payload, headers=headers)
    res = conn.getresponse()
    phantom.debug(f"Webhook response status: {res.status}")
    phantom.debug(f"Webhook response: {res.read().decode()}")

    ################################################################################
    ## Custom Code End
    ################################################################################

    return
