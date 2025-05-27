def run_user_script(script: str, data):
    local_vars = {}
    exec(script, {}, local_vars)
    if 'process' not in local_vars:
        raise ValueError("Script must define a 'process' function.")
    return local_vars['process'](data)
