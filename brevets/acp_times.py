"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
   Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
   """
   #BRACK = [200, 400, 600, 1000]
   hr = 0
   '''
   for b in BRACK:
      if control_dist_km <= b:
         hr += control_dist_km/34
         return arrow.now()
      else:
         hr += 200/34
   '''

   if control_dist_km <= 200:
      hr += control_dist_km/34
      brevet_start_time = brevet_start_time.shift(minutes=+round(hr*60))
      return arrow.get(brevet_start_time)
      #return brevet_start_time.shift(hours=+int(hr))
   else:
      hr += 200/34

   if control_dist_km <= 400:
      hr += (control_dist_km-200)/32
      brevet_start_time = brevet_start_time.shift(minutes=+round(hr*60))
      return arrow.get(brevet_start_time)
   else:
      hr += 200/32

   if control_dist_km <= 600:
      hr += (control_dist_km-400)/30
      brevet_start_time = brevet_start_time.shift(minutes=+int(hr*60))
      return arrow.get(brevet_start_time)
   else:
      hr += 200/30

   if control_dist_km <= 1000:
      hr += (control_dist_km-600)/28
      brevet_start_time = brevet_start_time.shift(minutes=+int(hr*60))
      return arrow.get(brevet_start_time)
   else:
      hr += 400/28
   
   hr += (control_dist_km-1000)/26
   brevet_start_time = brevet_start_time.shift(minutes=+int(hr*60))
   return arrow.get(brevet_start_time)

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
   Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
   """

   #BRACK = [200, 400, 600, 1000]
   hr = 0

   if control_dist_km <= 200:
      hr += control_dist_km/15
      brevet_start_time = brevet_start_time.shift(minutes=+round(hr*60))
      return arrow.get(brevet_start_time)
   else:
      hr += 200/15

   if control_dist_km <= 400:
      hr += (control_dist_km-200)/15
      brevet_start_time = brevet_start_time.shift(minutes=+round(hr*60))
      return arrow.get(brevet_start_time)
   else:
      hr += 200/15

   if control_dist_km <= 600:
      hr += (control_dist_km-400)/15
      brevet_start_time = brevet_start_time.shift(minutes=+int(hr*60))
      return arrow.get(brevet_start_time)
   else:
      hr += 200/15

   if control_dist_km <= 1000:
      hr += (control_dist_km-600)/11.428
      brevet_start_time = brevet_start_time.shift(minutes=+int(hr*60))
      return arrow.get(brevet_start_time)
   else:
      hr += 400/11.428
   
   hr += (control_dist_km-1000)/13.333
   brevet_start_time = brevet_start_time.shift(minutes=+int(hr*60))
   return arrow.get(brevet_start_time)

