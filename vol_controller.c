
// This #include statement was automatically added by the Particle IDE. #include "MQTT/MQTT.h"
// This #include statement was automatically added by the Particle IDE.
 #include "MQTT/MQTT.h"
#include "MQTT/MQTT.h"
// Define a pin that we'll place the pot on
int potPin = A5;

// Create a variable to hold the pot reading
int potReading = 0;

int reading = 0;
int flag =0;

//String sensor;
byte server[] = { 192,168,0,19 };//the IP of broker
void callback(char* topic, byte* payload, unsigned int length);
MQTT client(server, 1883, callback);
 
void callback(char* topic, byte* payload, unsigned int length) 
{
     char p[length + 1];
     memcpy(p, payload, length);
     p[length] = NULL;
     String message(p);
     delay(1000);
 }
void setup() 
{
     pinMode(A0,INPUT);
     RGB.control(true);
     client.connect(System.deviceID());
     if (client.isConnected()) {
         client.subscribe("volume");//volume is the topic that photon is subscribed
         //client.publish("fun", "hello");//publishing a data "hello" to the topic "fun"
     }
 }
void loop() 
{
    potReading = analogRead(potPin);
    reading = map(potReading, 0, 4095, 0, 100);
    if (reading != flag)
    {
      client.publish("volume",String(reading));
      flag = reading;
    }
     
 } 