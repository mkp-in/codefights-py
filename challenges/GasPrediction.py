def gasPrediction(driveDistances, currentGasLevel, avgMileage):
    s = sum(driveDistances)
    total_gallons_used = s / avgMileage
    avg_gas_spend_hour = total_gallons_used / 12.0
    if avg_gas_spend_hour <= currentGasLevel:
        return False
    return True


if __name__ == '__main__':
    print(gasPrediction([12, 6, 17, 5, 20], 0.25, 25))
    print(gasPrediction([120], 0.5, 10))
