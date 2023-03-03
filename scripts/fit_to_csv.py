import argparse
import sweat


COLUMN_TRANSLATIONS = {
    "enhanced_speed": "speed",
    "Cadence": "cadence",
    "step_length": "stride_length",
    "enhanced_altitude": "elevation",
}


COLUMNS_OF_INTEREST = [    "enhanced_speed",    "Cadence",    "cadence",    "step_length",    "heartrate",    "enhanced_altitude",    "latitude",    "longitude",    "core_temperature",    "skin_temperature",]


def fit_to_csv(fit_path, out_path):
    activity = sweat.read_fit(fit_path)

    activity = activity[[col for col in COLUMNS_OF_INTEREST if col in activity.columns]]
    activity.rename(columns=COLUMN_TRANSLATIONS, inplace=True)

    if "cadence" in activity.columns:
        del activity["Cadence"]

    activity["stride_length"] = activity["stride_length"] / 1000.0

    activity.to_csv(out_path, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert FIT file to CSV.")
    parser.add_argument("fit_path", help="path to FIT file")
    parser.add_argument("out_path", help="path to output CSV file")
    args = parser.parse_args()

    fit_to_csv(args.fit_path, args.out_path)
