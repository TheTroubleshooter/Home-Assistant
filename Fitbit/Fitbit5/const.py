"""Constants for the Fitbit platform."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.const import (
    CONF_CLIENT_ID,
    CONF_CLIENT_SECRET,
    LENGTH_FEET,
    MASS_KILOGRAMS,
    MASS_MILLIGRAMS,
    PERCENTAGE,
    TIME_MILLISECONDS,
    TIME_MINUTES,
)

ATTR_ACCESS_TOKEN: Final = "access_token"
ATTR_REFRESH_TOKEN: Final = "refresh_token"
ATTR_LAST_SAVED_AT: Final = "last_saved_at"

ATTR_DURATION: Final = "duration"
ATTR_DISTANCE: Final = "distance"
ATTR_ELEVATION: Final = "elevation"
ATTR_HEIGHT: Final = "height"
ATTR_WEIGHT: Final = "weight"
ATTR_BODY: Final = "body"
ATTR_LIQUIDS: Final = "liquids"
ATTR_BLOOD_GLUCOSE: Final = "blood glucose"
ATTR_BATTERY: Final = "battery"

CONF_MONITORED_RESOURCES: Final = "monitored_resources"
CONF_CLOCK_FORMAT: Final = "clock_format"
ATTRIBUTION: Final = "Data provided by Fitbit.com"

FITBIT_AUTH_CALLBACK_PATH: Final = "/api/fitbit5/callback"
FITBIT_AUTH_START: Final = "/api/fitbit5"
FITBIT_CONFIG_FILE: Final = "fitbit5.conf"
FITBIT_DEFAULT_RESOURCES: Final[list[str]] = ["activities/steps"]

DEFAULT_CONFIG: Final[dict[str, str]] = {
    CONF_CLIENT_ID: "CLIENT_ID_HERE",
    CONF_CLIENT_SECRET: "CLIENT_SECRET_HERE",
}
DEFAULT_CLOCK_FORMAT: Final = "12H"


@dataclass
class FitbitRequiredKeysMixin:
    """Mixin for required keys."""

    unit_type: str | None


@dataclass
class FitbitSensorEntityDescription(SensorEntityDescription, FitbitRequiredKeysMixin):
    """Describes Fitbit sensor entity."""


FITBIT_RESOURCES_LIST: Final[tuple[FitbitSensorEntityDescription, ...]] = (
    FitbitSensorEntityDescription(
        key="activities/activityCalories",
        name="Fitbit5 Activity Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/calories",
        name="Fitbit5 Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/caloriesBMR",
        name="Fitbit5 Calories BMR",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/distance",
        name="Fitbit5 Distance",
        unit_type="",
        icon="mdi:map-marker",
    ),
    FitbitSensorEntityDescription(
        key="activities/elevation",
        name="Fitbit5 Elevation",
        unit_type="",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/floors",
        name="Fitbit5 Floors",
        unit_type="floors",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/heart",
        name="Fitbit5 Resting Heart Rate",
        unit_type="bpm",
        icon="mdi:heart-pulse",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesFairlyActive",
        name="Fitbit5 Minutes Fairly Active",
        unit_type=TIME_MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesLightlyActive",
        name="Fitbit5 Minutes Lightly Active",
        unit_type=TIME_MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesSedentary",
        name="Fitbit5 Minutes Sedentary",
        unit_type=TIME_MINUTES,
        icon="mdi:seat-recline-normal",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesVeryActive",
        name="Fitbit5 Minutes Very Active",
        unit_type=TIME_MINUTES,
        icon="mdi:run",
    ),
    FitbitSensorEntityDescription(
        key="activities/steps",
        name="Fitbit5 Steps",
        unit_type="steps",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/activityCalories",
        name="Fitbit5 Tracker Activity Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/calories",
        name="Fitbit5 Tracker Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/distance",
        name="Fitbit5 Tracker Distance",
        unit_type="",
        icon="mdi:map-marker",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/elevation",
        name="Fitbit5 Tracker Elevation",
        unit_type="",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/floors",
        name="Fitbit5 Tracker Floors",
        unit_type="floors",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesFairlyActive",
        name="Fitbit5 Tracker Minutes Fairly Active",
        unit_type=TIME_MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesLightlyActive",
        name="Fitbit5 Tracker Minutes Lightly Active",
        unit_type=TIME_MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesSedentary",
        name="Fitbit5 Tracker Minutes Sedentary",
        unit_type=TIME_MINUTES,
        icon="mdi:seat-recline-normal",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesVeryActive",
        name="Fitbit5 Tracker Minutes Very Active",
        unit_type=TIME_MINUTES,
        icon="mdi:run",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/steps",
        name="Fitbit5 Tracker Steps",
        unit_type="steps",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="body/bmi",
        name="Fitbit5 BMI",
        unit_type="BMI",
        icon="mdi:human",
    ),
    FitbitSensorEntityDescription(
        key="body/fat",
        name="Fitbit5 Body Fat",
        unit_type=PERCENTAGE,
        icon="mdi:human",
    ),
    FitbitSensorEntityDescription(
        key="body/weight",
        name="Fitbit5 Weight",
        unit_type="",
        icon="mdi:human",
    ),
    FitbitSensorEntityDescription(
        key="sleep/awakeningsCount",
        name="Fitbit5 Awakenings Count",
        unit_type="times awaken",
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/efficiency",
        name="Fitbit5 Sleep Efficiency",
        unit_type=PERCENTAGE,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesAfterWakeup",
        name="Fitbit5 Minutes After Wakeup",
        unit_type=TIME_MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesAsleep",
        name="Fitbit5 Sleep Minutes Asleep",
        unit_type=TIME_MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesAwake",
        name="Fitbit5 Sleep Minutes Awake",
        unit_type=TIME_MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesToFallAsleep",
        name="Fitbit5 Sleep Minutes to Fall Asleep",
        unit_type=TIME_MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/startTime",
        name="Fitbit5 Sleep Start Time",
        unit_type=None,
        icon="mdi:clock",
    ),
    FitbitSensorEntityDescription(
        key="sleep/timeInBed",
        name="Fitbit5 Sleep Time in Bed",
        unit_type=TIME_MINUTES,
        icon="mdi:hotel",
    ),
)

FITBIT_RESOURCE_BATTERY = FitbitSensorEntityDescription(
    key="devices/battery",
    name="Fitbit5 Battery",
    unit_type=None,
    icon="mdi:battery",
)

FITBIT_RESOURCES_KEYS: Final[list[str]] = [
    desc.key for desc in (*FITBIT_RESOURCES_LIST, FITBIT_RESOURCE_BATTERY)
]

FITBIT_MEASUREMENTS: Final[dict[str, dict[str, str]]] = {
    "en_US": {
        ATTR_DURATION: TIME_MILLISECONDS,
        ATTR_DISTANCE: "mi",
        ATTR_ELEVATION: LENGTH_FEET,
        ATTR_HEIGHT: "in",
        ATTR_WEIGHT: "lbs",
        ATTR_BODY: "in",
        ATTR_LIQUIDS: "fl. oz.",
        ATTR_BLOOD_GLUCOSE: f"{MASS_MILLIGRAMS}/dL",
        ATTR_BATTERY: "",
    },
    "en_GB": {
        ATTR_DURATION: TIME_MILLISECONDS,
        ATTR_DISTANCE: "kilometers",
        ATTR_ELEVATION: "meters",
        ATTR_HEIGHT: "centimeters",
        ATTR_WEIGHT: "stone",
        ATTR_BODY: "centimeters",
        ATTR_LIQUIDS: "milliliters",
        ATTR_BLOOD_GLUCOSE: "mmol/L",
        ATTR_BATTERY: "",
    },
    "metric": {
        ATTR_DURATION: TIME_MILLISECONDS,
        ATTR_DISTANCE: "kilometers",
        ATTR_ELEVATION: "meters",
        ATTR_HEIGHT: "centimeters",
        ATTR_WEIGHT: MASS_KILOGRAMS,
        ATTR_BODY: "centimeters",
        ATTR_LIQUIDS: "milliliters",
        ATTR_BLOOD_GLUCOSE: "mmol/L",
        ATTR_BATTERY: "",
    },
}

BATTERY_LEVELS: Final[dict[str, int]] = {
    "High": 100,
    "Medium": 50,
    "Low": 20,
    "Empty": 0,
}
