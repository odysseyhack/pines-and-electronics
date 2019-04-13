#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import logging
import time
from datetime import datetime
from threading import Thread

from squid_py.keeper.contract_handler import ContractHandler
from squid_py.keeper.event_filter import EventFilter

logger = logging.getLogger(__name__)


class EventListener(object):
    """Class representing an event listener."""

    def __init__(self, contract, event_name, args=None, from_block=0, to_block='latest',
                 filters=None):
        contract = contract
        self.event_name = event_name
        self.event = getattr(contract.events, event_name)
        self.filters = filters if filters else {}
        self.from_block = from_block
        self.to_block = to_block
        self.event_filter = self.make_event_filter()
        self.event_filter.poll_interval = 0.5
        self.timeout = 60  # seconds
        self.args = args

    def make_event_filter(self):
        """Create a new event filter."""
        event_filter = EventFilter(
            self.event_name,
            self.event,
            self.filters,
            from_block=self.from_block,
            to_block=self.to_block
        )
        event_filter.set_poll_interval(0.5)
        return event_filter

    def listen_once(self, callback, timeout=None, timeout_callback=None, start_time=None,
                    blocking=False):
        """

        :param callback: a callback function that takes one argument the event dict
        :param timeout: float timeout in seconds
        :param timeout_callback: a callback function when timeout expires
        :param start_time: float start time in seconds, defaults to current time and is used
            for calculating timeout
        :param blocking: bool blocks this call until the event is detected
        :return: event if blocking is True and an event is received, otherwise returns None
        """
        events = []
        original_callback = callback

        def _callback(event):
            events.append(event)
            original_callback(event)

        if blocking:
            callback = _callback
        # TODO Review where to close this threads.
        Thread(
            target=self.watch_one_event,
            args=(self.event_filter,
                  callback,
                  timeout_callback,
                  timeout if timeout is not None else self.timeout,
                  self.args,
                  start_time),
            daemon=True,
        ).start()
        if blocking:
            while not events:
                time.sleep(0.2)

            return events[0]

        return None

    def watch_one_event(self, event_filter, callback, timeout_callback, timeout, args,
                        start_time=None):
        """
        Start to watch one event.

        :param event_filter:
        :param callback:
        :param timeout_callback:
        :param timeout:
        :param args:
        :param start_time:
        :return:
        """
        if timeout and not start_time:
            start_time = int(datetime.now().timestamp())

        if not args:
            args = []

        while True:
            try:
                events = event_filter.get_all_entries()
                if events:
                    callback(events[0], *args)
                    return

            except (ValueError, Exception) as err:
                # ignore error, but log it
                logger.debug(f'Got error grabbing keeper events: {str(err)}')

            time.sleep(0.1)
            if timeout:
                elapsed = int(datetime.now().timestamp()) - start_time
                if elapsed > timeout:
                    if timeout_callback:
                        timeout_callback(*args)
                    else:
                        callback(None, *args)
                    break
