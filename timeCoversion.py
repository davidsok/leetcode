def timeConversion(s):
    ans = ''
    if s[-2:] == 'AM':
        ans = s[:-2] if int(s[:2])+12 != 24 else '00'+s[2:-2]
    if s[-2:] == 'PM':
        ans = str(int(s[:2])+12)+s[2:-2] if int(s[:2])+12 != 24 else '12'+s[2:-2]
    print(ans)
    return ans

timeConversion('07:01:01AM')
timeConversion('12:40:22AM')
timeConversion('12:40:22PM')