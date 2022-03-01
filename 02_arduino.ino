void setup(){
    Serial.begin(115200);
}
void loop(){
    int luz = analogRead(5);//Leitura de sinal analógico
    Serial.println(luz);
    delay(5000);
}