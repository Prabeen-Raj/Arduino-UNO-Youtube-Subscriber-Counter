# Import Module

from googleapiclient.discovery import build
import serial

s = serial.Serial('COM3', baudrate=9600) #Enter Arduino Port Number

# Create YouTube Object
if s.isOpen():
     while (True):
          youtube = build('youtube', 'v3',
				developerKey='Enter API KEY') #Enter API key
          ch_request = youtube.channels().list(
	part='statistics',
	id='Enter Channel ID') #Enter Channel ID
          ch_response = ch_request.execute()
          sub = ch_response['items'][0]['statistics']['subscriberCount']
          print("Subscriber:- " + sub )
          s.write(sub.encode())
          print(type(sub))

    


