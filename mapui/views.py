from django.shortcuts import render,HttpResponse
import math



def modis(north_lat,south_lat,west_lng,east_lng):
    
    x1 = math.ceil((west_lng-21)/2)
    x2 = math.ceil((east_lng-21)/2)
    
    north_lat += 89
    south_Lat += 89
    
    y1 = math.floor((south_lat)/2)
    y2 = math.floor((north_lat)/2)
    
    return x1,x2,y1,y2
        
        
        
        


def map_home(request):
    
    
    
    base_url = 'http://test.opendap.org/opendap/data/nc/coads_climatology.nc.ascii?'
    
    return render(request, 'home/mapui.html',{'url':base_url})


def f(request):
    
    base_url = 'http://test.opendap.org/opendap/data/nc/coads_climatology.nc.ascii?'
    
    user_request = request.GET.get('lat_from')
    
    
    url = base_url + user_request
    
    context={'url':url}
    
    return 
