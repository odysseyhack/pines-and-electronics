from backend.car.car_controller import CarController


def test_car_controller():
    car = CarController()
    send_command = car.send_command('Forward')
    assert send_command
    filter = car.contract.events.CarCommandSent.createFilter(fromBlock=0, toBlock='latest')
    car.contract.functions.sendCommand("k").transact()
    logs = filter.get_all_entries()
    assert len(logs) > 0
    event = car.subscribe_to_command_event(
        20,
        car.log_event(car.COMMAND_SENT_EVENT),
        (),
        wait=True
    )
    assert event, 'no event for command_sent_event'
