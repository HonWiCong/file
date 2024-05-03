import time  #Import time library
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("MyCloudComputer")
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 8883)
myMQTTClient.configureEndpoint("a2oe62hw04z5mw-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/ubuntu/swe30011/cert/AmazonRootCA1.pem", "/home/ubuntu/swe30011/cert/fedce8b09d58243bbb5f51549a7b78c5aee33f9436fb7e43f1e99c40f3dc6f53-private.pem.key", "/home/ubuntu/swe30011/cert/fedce8b09d58243bbb5f51549a7b78c5aee33f9436fb7e43f1e99c40f3dc6f53-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

#connect and publish
myMQTTClient.connect()
myMQTTClient.publish("cloud/info", "connected", 0)
#myMQTTClient.publish("xxxx/info", "connected", 0)

while 1:
    time.sleep(2)  #Delay of 2 seconds
    
    value = 200
    payload = '{"cloud message: ":'+ str(value) +'}'
    print (payload)
    myMQTTClient.publish("cloud/data", payload, 0)
