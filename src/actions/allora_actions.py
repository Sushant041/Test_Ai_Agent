import logging
import csv
from src.action_handler import register_action
from src.helpers import print_h_bar

@register_action("send-csv-to-allora")
def send_csv_to_allora(agent, **kwargs):
    try:
        # Extract CSV data
        csv_data = kwargs.get('csv_data', None)
        if not csv_data:
            agent.logger.error("No CSV data provided.")
            return None
        
        agent.logger.info("Sending CSV data to Allora for analysis.")

        # Assuming the CSV data is passed as a list of dictionaries
        response = agent.connection_manager.perform_action(
            connection_name="allora",  # Allora connection in your manager
            action_name="analyze-csv",  # Assuming 'analyze-csv' is an action in your connection
            params=[csv_data]  # Passing the CSV data as a parameter
        )

        if response:
            agent.logger.info(f"Allora's response: {response}")
            return response
        else:
            agent.logger.error("No response received from Allora.")
            return None
    except Exception as e:
        agent.logger.error(f"Error occurred while sending CSV to Allora: {e}")
        return None
