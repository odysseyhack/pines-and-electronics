pragma solidity 0.5.3;

/**
 * @title Car Controller
 * @author Pines & Electronics
 *
 * @dev Simple contract emitting an event.
 */
contract CarController {


    /**
     * @dev CarCommandSent event register in the log the commands that you send to the car.
     */
    event CarCommandSent(
        string _command
    );

    /**
     * @notice Send command
     *
     * @dev send the event with the car command.
     *
     * @param _command refers to the attribute value, limited to 2048 bytes.
     * @return true when the command was emitted properly.
     */
    function sendCommand (
        string memory _command
    )
        public
        returns (bool commandSent)
    {

        emit CarCommandSent(
            _command
        );

        return true;
    }

}
