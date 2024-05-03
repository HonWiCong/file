import time  #Import time library
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID")
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 8883)
myMQTTClient.configureEndpoint("your_endpoint", 8883)
myMQTTClient.configureCredentials("/home/pi/cert/AmazonRootCA1.pem", "/home/pi/cert/xxxx-private.pem.key", "/home/pi/cert/xxxxx-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

#connect and publish
myMQTTClient.connect()
myMQTTClient.publish("rpi/info", "connected", 0)
#myMQTTClient.publish("xxxx/info", "connected", 0)

while 1:
    time.sleep(2)  #Delay of 2 seconds
    
    value = 100
    payload = '{"wiper":'+ str(value) +'}'
    print payload
    myMQTTClient.publish("rpi/data", payload, 0)
