@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################
    import pkgutil

    libs = sorted([module.name for module in pkgutil.iter_modules()])
    phantom.debug("Installed Python libraries:")
    for lib in libs:
        phantom.debug(lib)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return
