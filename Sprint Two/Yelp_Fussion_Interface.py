import requests
import json



def access_API(name):

    #unique key to access API & dict 'headers' to access API via unique key 
    api_key = 'ozFbeHZhNgSDjqO2NE6dB4w0oI-UtOEy-cnVXSOlUMwuAj_MaF_1D9I3VF17a7H2j9cvJheUzNjEVgCwnZ_J9LQ7486uzuAL5p5T1FEXjJntV4oBjQoU9r-Mz70yYnYx'
    header = {                                                                 
            'Authorization': 'Bearer %s' % api_key                          
    }


    url='https://api.yelp.com/v3/businesses/search'                             #url linking to search feature

    parameters = {                                                              #constraints for Yelp search
        'term' : name,
        'location'   : "New Brunswick, NJ",
        'radius'     : 10*1609,
        'categories' : ""
    }
 
    req = requests.get(url,params=parameters,headers = header)                  #makes get request 
    if (req.status_code !=200):                                                 #print status code if error occured
        print("Status Code is",req.status_code)
        
    doctors = json.loads(req.text)                                      #returns text of request as dict
    doc_list = [""] * len(doctors["businesses"])

    for i in range(len(doctors['businesses'])):                                #run thru bar dict
        doc_list[i] = doctors['businesses'][i]['name']                        #store bar names in bar_name_list
        #print(doc_list[i])


    return doctors

def main():
    print("\n\n\n---------------------------------------------------------------")
    #access_API()



if __name__ == "__main__":
    main()