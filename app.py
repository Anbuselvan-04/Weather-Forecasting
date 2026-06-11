from forecast import make_prediction

def main():

    print("=" * 50)
    print("WEATHER FORECASTING SYSTEM")
    print("=" * 50)

    while True:

        print("\nOptions:")
        print("temperature")
        print("humidity")
        print("windspeed")
        print("all")
        print("exit")

        parameter = input(
            "\nEnter weather parameter: "
        ).lower()

        if parameter == "exit":
            break

        month = input(
            "Enter forecast month (January-December): "
        ).capitalize()

        result = make_prediction(
            parameter,
            month
        )

        print("\nForecast Result\n")
        print(result.to_string(index=False))

        print("\nGraph saved as output.png")


if __name__ == "__main__":
    main()