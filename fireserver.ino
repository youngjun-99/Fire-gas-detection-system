#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

int fire = D6;
int gas = A0;

const char* ssid = "iptime";
const char* password = "123456789a";

ESP8266WebServer server(80); // 서버 생성

void setup() {
  pinMode(gas, INPUT);
  pinMode(fire, INPUT);
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

  server.on("/api/data", HTTP_GET, handleDataRequest);  // "/api/data" 경로에 대한 요청 처리 설정
  server.begin();
  Serial.println("Server started");
}

void loop() {
  server.handleClient();  // 클라이언트 요청 처리
}

void handleDataRequest() {
  float gasvalue = analogRead(gas);
  float firevalue = digitalRead(fire);
  Serial.print("gas: ");
  Serial.println(gasvalue);
  Serial.print("fire: ");
  Serial.println(firevalue);

  String jsonResponse = "{\"fire\": " + String(firevalue) + ", \"gas\": " + String(gasvalue) + "}";
  server.send(200, "application/json", jsonResponse);
}
