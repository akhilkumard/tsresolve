# Tsresolve (Timestamp resolve)

Timestamp generator for either "Point of time" or "Duration of time" from Text (string). This uses recurrent, parsedatetime libraries to detect dates from strings. However, there are lot of major updations in this library which will allow user to generate either point of time or duration between two point of times.

#### Points to know:
1. It generates time stamps in ISO format.
2. When no ammod (last/previous/next..) is used before month/year, it detects the passed one.
   Ex: Show calls from December 5th. (If you are asking this before December 5th 2018, it detects December 5th 2017 else, December 5th 2018). Test it with and without ammods for better understanding.

##### Examples:

Point of time: Expected result will be (Timestamp, Bool). Bool is "True" if time detected in phrase. Else, "False"

1. November 3rd at 3 p.m. | Result: (2019-11-03T15:00:00, True)
2. next monday evening at 5 o'clock | Result: (2018-12-24T17:00:00, True)
3. last saturday | Result: (2018-12-24T17:00:00, False)

Period of time: Expected result will be (Start timestamp, End timestamp)

1. from last tuesday till date | Result: ('2018-12-11T00:00:00', '2018-12-18T23:59:59')
2. from last november 5th to december 15th | Result: ('2018-11-01T00:00:00', '2018-12-18T23:59:59')
3. show something from november 5th 2017 | Result: ('2017-11-05T00:00:00', '2017-11-05T23:59:59')

#### Not handled:
1. Duration between two years. Ex: 2018-2019
2. Currently not handling "5th of January" format.
3. Time level is currently handled only in point of time, yet to be handled in period of time.

#### Credits
Tsresolve is inspired by Recurrent. It also uses the parsedatetime library for creating timestamps.

#### Author
Akhil kumar D (akhilkumar.doppalapudi@gmail.com)