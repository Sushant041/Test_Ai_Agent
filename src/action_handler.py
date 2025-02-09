import logging

logger = logging.getLogger("action_handler")

action_registry = {}    

def register_action(action_name):
    def decorator(func):
        action_registry[action_name] = func
        logger.info(f"Action '{action_name}' registered successfully.")
        return func
    return decorator

def execute_action(agent, action_name, **kwargs):
    if action_name in action_registry:
        try:
            logger.info(f"Executing action '{action_name}' with parameters: {kwargs}")
            return action_registry[action_name](agent, **kwargs)
        except Exception as e:
            logger.error(f"Error executing action '{action_name}': {str(e)}")
            return None
    else:
        logger.error(f"Action '{action_name}' not found")
        return None
