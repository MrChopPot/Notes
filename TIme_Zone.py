from timezonefinder import TimezoneFinder

tf = TimezoneFinder(in_memory=True)
TimezoneFinder.using_numba()

def getTimezone(df): 
    timezone = tf.timezone_at(lng = df['deviceLongitude'],lat = df['deviceLatitude'])
    return timezone

def getLocaltime(df):
    localtime = df['time'].tz_convert(df['timezone'])
    return localtime

ua_geo['timezone'] = ua_geo.apply(getTimezone, axis = 1)

ua_geo['time'] = pd.DatetimeIndex(pd.to_datetime(ua_geo['UTCtimestamp'], unit = 'ms')).tz_localize('UTC')
ua_geo['time'] = ua_geo.apply(getLocaltime, axis = 1)