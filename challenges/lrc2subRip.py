"""
https://app.codesignal.com/challenge/deMCqfKThepek7YMH

During your most recent trip to Codelandia you decided to buy a brand new CodePlayer, a music player that (allegedly) can work with any possible media format. As it turns out, this isn't true: the player can't read lyrics written in the LRC format. It can, however, read the SubRip format, so now you want to translate all the lyrics you have from LRC to SubRip.

Since you are a pro programmer (no noob would ever get to Codelandia!), you're happy to implement a function that, given lrcLyrics and songLength, returns the lyrics in SubRip format.

Example

For

lrcLyrics = ["[00:12.00] Happy birthday dear coder,",
             "[00:17.20] Happy birthday to you!"]
and songLength = "00:00:20", the output should be

lrc2subRip(lrcLyrics, songLength) = [
  "1",
  "00:00:12,000 --> 00:00:17,200",
  "Happy birthday dear coder,",
  "",
  "2",
  "00:00:17,200 --> 00:00:20,000",
  "Happy birthday to you!"
]

"""


def lrc2subRip(lrcLyrics, songLength):
    def parse_time(s):
        s = s.replace(".", ",")
        s = s[3:] + "0"
        return s

    ret = []
    for i,j in enumerate(lrcLyrics):
        t = j[1:9]
        t = parse_time(t)
        ret.append(str(i+1))
        if i == len(lrcLyrics) - 1:
            next = parse_time(songLength[1:6] + "." + songLength[7:])
        else:
            next = parse_time(lrcLyrics[i+1][1:9])

        ret.append(t + " --> "+next)
        ret.append(j[11:])
        if i < len(lrcLyrics) - 1:
            ret.append("")

    return ret


if __name__ == '__main__':
    print(lrc2subRip(["[00:12.00] Happy birthday dear coder,", "[00:17.20] Happy birthday to you!"], "00:00:20"))
