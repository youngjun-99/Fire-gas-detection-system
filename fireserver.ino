#include <ESP8266WiFi.h>

int fire = D6;
int gas = A0;

const char* ssid = "iptime";
const char* password = "123456789a";

WiFiServer server(80);
WiFiClient client;
 
void setup() {
  pinMode(gas ,INPUT);
  pinMode(fire ,INPUT);
  Serial.begin(115200);
 
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connecting to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
 
  server.begin();
  Serial.println("Server started");
}
 
void loop() {
  client = server.available();
  if(!client) return;
  float gasvalue = analogRead(gas);
  float firevalue = digitalRead(fire);
  Serial.print("gas:");
  Serial.println(gasvalue);
  Serial.print("fire:");
  Serial.println(firevalue);
  Serial.println("새로운 클라이언트");
  client.setTimeout(5000);
 
  String request = client.readStringUntil('\r');
  Serial.println("request: ");
  Serial.println(request);
 
  while(client.available()) {
    client.read();
  }
  client.print("HTTP/1.1 200 OK");
  client.print("Content-Type: text/html\r\n\r\n");
  client.print("<!DOCTYPE HTML>");
  client.print("<html>");
  client.print("<head>"); 
  client.print("<meta charset=\"UTF-8\" http-equiv=\"refresh\" content=\"1\">");
  client.print("<title>fire senrsor Webpage</title>");
  client.print("</head>");
  client.print("<body>");
  client.print("<h2>fire senrsor Webpage</h2>");
  client.print("<br>");
  client.print("fire : ");
  client.print("<span class=\"fire\">");
  client.print("<em class=\"num_fire\">");
  client.print(firevalue);
  client.print("</em>");
  client.print("<br>");  
  client.print("gas : ");
  client.print("</span>");
  client.print("<span class=\"gas\">");
  client.print("<em class=\"num_gas\">");
  client.print(gasvalue);
  client.print("</em>");
  client.print("</span>");
  client.print("</body>");
  client.print("</html>");
  delay(5000);
  Serial.println("클라이언트 연결 해제");
}
