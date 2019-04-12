/* globals artifacts */
const CarController = artifacts.require('CarController')

// dummy owner, replace with real wallet/owner
const owner = '0xeE9300b7961e0a01d9f0adb863C7A227A07AaD75'

module.exports = function(deployer) {
    deployer.deploy(CarController, owner)
}
