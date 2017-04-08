class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]


        Hours (0-11):
        8   4   2   1

        Minutes (0-59):
        32  16  8   4   2   1

        Given number of led light on, what times can the watch represent?

        C(10, num)s
        """
        LEDS = ['8h', '4h', '2h', '1h', '32m', '16m', '8m', '4m', '2m', '1m']

        times = []
        from itertools import combinations
        for leds in combinations(LEDS, num):
            display_time = self.display(leds)
            if display_time:
                times.append(display_time)
        return times

    def display(self, leds):
        hours = 0
        minutes = 0
        for led in leds:
            # No pop method for string. Use the following.
            led, time_unit = led[:-1], led[-1]

            if time_unit == 'h':
                hours += int(led)
            else:
                minutes += int(led)

        if hours > 11 or minutes > 59:
            return None
        return '%d:%02d' % (hours, minutes)
