from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect

import math

BASE_URL1 = 'http://test.opendap.org/opendap/data/nc/coads_climatology.nc.ascii?'
BASE_URL2 = 'http://test.opendap.org/opendap/noaa_pathfinder/2005001-2005008.s0484pfv50-sst.hdf.ascii?'
#alogorithm to map coordiates to index values

def coads(north_lat,south_lat,west_lng,east_lng):

    if west_lng < 0:
        west_lng = 360 + (west_lng)

    if east_lng < 0:
        east_lng = 360 +(east_lng)

    if west_lng < 21:
        west_lng = 21

    if east_lng < 21:
        east_lng = 21


    x1 = math.ceil((west_lng-21)/2)
    x2 = math.floor((east_lng-21)/2)

    if x1>x2:
        x1,x2=x2,x1

    north_lat += 89
    south_lat += 89

    y1 = math.floor((south_lat)/2)
    y2 = math.ceil((north_lat)/2)

    return x1,x2,y1,y2

#pathfider data alogorithm

def pathfinder(north_lat,south_lat,west_lng,east_lng):
    north_most =89.9800033569336
    west_most = -179.981979370117

    lat_diff = 0.043946775858
    lng_diff = 0.043919452103

    x1= math.floor((north_most-north_lat)/lat_diff)
    x2 = math.floor((north_most-south_lat)/lat_diff)

    y1 = math.floor((west_lng-west_most)/lng_diff)
    y2 = math.floor((east_lng-west_most)/lng_diff)

    return x1,x2,y1,y2
#construct url from coordinates

def get_url(request):

    n_lat = request.POST.get('lat_from')
    s_lat = request.POST.get('lat_to')
    w_lng = request.POST.get('lng_from')
    e_lng = request.POST.get('lng_to')

    category = request.POST.get('category')
    data = request.POST.get('data')
    time_start = request.POST.get('time_start')
    time_end = request.POST.get('time_end')

    time_start =int(time_start.split('-')[1])-1
    time_end = int(time_end.split('-')[1])-1

    if time_end < time_start:
        raise  Exception("Start Month has greater value than End Month !!")

    ## DEBUG:
    print(data)
    print(category)

    if data == 'COADS':
        x1,x2,y1,y2 = coads(float(n_lat),float(s_lat),float(w_lng),float(e_lng))
        request_url = BASE_URL1 + category +'[{}:1:{}][{}:1:{}][{}:1:{}]'.format(time_start,time_end,y1,y2,x1,x2)

    else:
        x1,x2,y1,y2 = pathfinder(float(n_lat),float(s_lat),float(w_lng),float(e_lng))
        request_url = BASE_URL2 + 'sst' +'[{}:1:{}][{}:1:{}]'.format(x1,x2,y1,y2)+',lat[{}:1:{}]'.format(x1,x2)+',lon[{}:1:{}]'.format(y1,y2)


    return request_url

def map_home(request):

    if request.method == 'POST':

        url = get_url(request)
        print(url)
        return redirect(url)

    return render(request, 'home/mapui.html')
