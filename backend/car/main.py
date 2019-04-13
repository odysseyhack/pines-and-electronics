from backend.car.car_controller import CarController

class main():
    car = CarController()
    last_block_number = 0
    while True:
        filter = car.contract.events.CarCommandSent.createFilter(fromBlock=0, toBlock='latest')
        logs = filter.get_all_entries()
        block_number = logs[-1].blockNumber
        if block_number != last_block_number:
            car.execute_command(car.parse_command(logs[-1]))
            last_block_number= block_number


if __name__ == '__main__':
    main()