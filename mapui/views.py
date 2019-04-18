from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from .forms import Query
import math


BASE_URL = 'http://test.opendap.org/opendap/data/nc/coads_climatology.nc.ascii?'

#alogorithm to map coordiates to index values

def modis(north_lat,south_lat,west_lng,east_lng):
    
    if west_lng < 0:
        west_lng = 90 - (west_lng)
    if east_lng < 0:
        east_lng = 90 - (east_lng)
    
    x1 = math.ceil((west_lng-21)/2)
    x2 = math.ceil((east_lng-21)/2)
    
    if x1>x2:
        x1,x2=x2,x1
    
    north_lat += 89
    south_lat += 89
    
    y1 = math.floor((south_lat)/2)
    y2 = math.floor((north_lat)/2)
    
    return x1,x2,y1,y2
        
        
        
#construct url from coordinates        
    
def get_url(request):
    
    
    
    n_lat = request.POST.get('lat_from')
    s_lat = request.POST.get('lat_to')
    w_lng = request.POST.get('lng_from')
    e_lng = request.POST.get('lng_to')
    
    category = 'SST'
    
    
    
    x1,x2,y1,y2 = modis(float(n_lat),float(s_lat),float(w_lng),float(e_lng))
    
    request_url = BASE_URL + category +'[0:1:11][{}:1:{}][{}:1:{}]'.format(y1,y2,x1,x2)
    
    return request_url




def map_home(request):
    
    
    if request.method == 'POST':
        
        url = get_url(request)
        print(url)
        return redirect(url)

   
    return render(request, 'home/mapui.html')

    

    
    
    
    
   
