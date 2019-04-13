import json
import logging
import requests

from car.event_listener import EventListener
from squid_py.config import Config
from squid_py.config_provider import ConfigProvider
from squid_py.keeper.web3_provider import Web3Provider
from web3.contract import ConciseContract


class CarController:
    CONTRACT_NAME = 'CarController'

    def __init__(self):
        self.config = Config('config.ini')
        self.COMMAND_SENT_EVENT = 'CarCommandSent'
        ConfigProvider.set_config(self.config)

    @property
    def contract(self):
        return Web3Provider.get_web3().eth.contract(
            address=self.config.get('resources', 'car.contract.address'),
            abi=self.get_abi('artifacts/CarController.json')['abi']
        )

    @property
    def contract_concise(self):
        return ConciseContract(Web3Provider.get_web3().eth.contract(
            address=self.config.get('resources', 'car.contract.address'),
            abi=self.get_abi('artifacts/CarController.json')['abi']
        ))

    @staticmethod
    def get_abi(path):
        with open(path) as f:
            contract_dict = json.loads(f.read())
            return contract_dict

    def send_command(self, command):
        """

        :param command:
        :return:
        """
        logging.info(f'Sending commnad {command} to the car.')
        return self.contract.functions.sendCommand(command).transact()

    def subscribe_to_event(self, event_name, timeout, event_filter, callback=False,
                           timeout_callback=None, args=None, wait=False):
        return EventListener(
            self.contract,
            event_name,
            args,
            filters=event_filter
        ).listen_once(
            callback,
            timeout_callback=timeout_callback,
            timeout=timeout,
            blocking=wait
        )

    def subscribe_to_command_event(self, timeout, callback, args, wait=False):
        return self.subscribe_to_event(
            self.COMMAND_SENT_EVENT,
            timeout,
            # {'_command': 'Forward'},
            None,
            callback=callback,
            args=args,
            wait=wait
        )

    @staticmethod
    def log_event(event_name):
        def _process_event(event):
            print(f'Received event {event_name}: {event}')
        return _process_event

    def parse_command(self, event):
        if event is None:
            logging.error('No event to parse.')
        if event.args is None:
            logging.info('There are no commnads in this event')
        command = event.args._command
        return command

    def execute_command(self, command):
        logging.info(f'Calling command:{command}')
        if command.startswith('status'):
            requests.get(f'{self.config.get("resources","raspberry.url")}/api/status')
        elif command.startswith('snap'):
            requests.get(f'{self.config.get("resources", "raspberry.url")}/api/snap')
        elif command.startswith('register'):
            requests.post(f'{self.config.get("resources", "raspberry.url")}/api/register')
        elif command.startswith('snapshot'):
            requests.get(f'{self.config.get("resources", "raspberry.url")}/api/snapshot')
        elif command.startswith('linear'):
            requests.get(f'{self.config.get("resources", "raspberry.url")}/api/linear')
        elif command.startswith('steer'):
            requests.get(f'{self.config.get("resources", "raspberry.url")}/api/steer')
        else:
            logging.error(f'Invalid command: {command}')

    # def do_request(self):
    #     try:
    #         requests.get(f'{self.config.get("resources", "raspberry.url")}/api/snapshot')
    #     except:
