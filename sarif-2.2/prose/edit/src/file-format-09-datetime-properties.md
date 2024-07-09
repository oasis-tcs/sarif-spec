## Date/time properties{#datetime-properties}

Certain properties in this document specify a date and time. The value of every such property, if present, **SHALL** be a string in the following format, which is compatible with the ISO standard for date and time formats [cite](#ISO8601;2004):

    date time = date, [ "T", time, "Z" ] (* UTC time *);

    date = year, "-", month, "-", day;

    year = 4 * decimal digit;

    month = 2 * decimal digit (* from 01 to 12 *);

    day = 2 * decimal digit (* from 01 to 31 *);

    time = hour, ":", minute, [ ":", second, [ ".", fraction ] ];

    hour = 2 * decimal digit (* from 00 to 24, to represent midnight at the
                                end of a calendar day *);

    minute = 2 * decimal digit (* from 00 to 59 *);

    second = 2 * decimal digit (* from 00 to 60, to accommodate leap second *);

    fraction = decimal digit, { decimal digit };

&emsp;&emsp;EXAMPLES:

&emsp;&emsp;`2016-02-08`

&emsp;&emsp;`2016-02-08T16:08Z`

&emsp;&emsp;`2016-02-08T16:08:25Z`

&emsp;&emsp;`2016-02-08T16:08:25.943Z`

&emsp;&emsp;`2016-02-08T00:00:00Z`

&emsp;&emsp;`2016-02-08T16:08:00Z`

&emsp;&emsp;`2016-02-08T16:08:25Z`

&emsp;&emsp;`2016-02-08T16:08:25.943Z`

The time component of every date/time-valued property **SHALL** be expressed in Coordinated Universal Time (UTC).

> NOTE 1: The name of every date/time-valued property ends in "Utc" to emphasize that requirement.

The time components of date/time-valued properties in property bags ([sec](#property-bags)) **SHOULD** also be expressed in UTC.

> NOTE 2: This might not always be possible if the property comes from a source that does not provide time zone information.

A SARIF producer **SHOULD NOT** provide more digits in `fraction` than warranted by the precision of the clock on the computer on which it runs.

A SARIF producer **SHOULD** express date/time properties, except for those that express product release dates, to a precision of at least whole seconds.
